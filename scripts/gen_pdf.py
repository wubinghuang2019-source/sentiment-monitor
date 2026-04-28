#!/usr/bin/env python3
"""
舆情报告 PDF 生成脚本
当用户需要 PDF 格式的舆情报告时使用此脚本。

用法: python scripts/gen_pdf.py --html /path/to/report.html --output /path/to/output.pdf
"""

import argparse
import os
import sys

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm, cm
    from reportlab.lib.colors import HexColor
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
except ImportError:
    print("需要安装 reportlab: pip install reportlab")
    sys.exit(1)

# 尝试注册中文字体
FONT_NAME = None
FONT_BOLD_NAME = None

def register_chinese_font():
    """尝试注册系统中可用的中文字体"""
    global FONT_NAME, FONT_BOLD_NAME

    font_candidates = [
        # macOS
        ("/System/Library/Fonts/PingFang.ttc", "PingFang"),
        ("/System/Library/Fonts/STHeiti Medium.ttc", "STHeiti"),
        ("/System/Library/Fonts/Hiragino Sans GB.ttc", "HiraginoSansGB"),
        # Linux
        ("/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc", "NotoSansCJK"),
        ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", "NotoSansCJK"),
        # Windows
        ("C:\\Windows\\Fonts\\msyh.ttc", "MicrosoftYaHei"),
    ]

    for path, name in font_candidates:
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont(name, path))
                FONT_NAME = name
                FONT_BOLD_NAME = name
                return True
            except Exception:
                continue

    # 尝试 reportlab 内置
    try:
        from reportlab.pdfbase.cidfonts import UnicodeCIDFont
        pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
        FONT_NAME = 'STSong-Light'
        FONT_BOLD_NAME = 'STSong-Light'
        return True
    except Exception:
        pass

    return False

# 颜色定义
COLOR_PRIMARY = HexColor('#1a1a2e')
COLOR_SECONDARY = HexColor('#16213e')
COLOR_ACCENT = HexColor('#0f3460')
COLOR_POSITIVE = HexColor('#27ae60')
COLOR_NEGATIVE = HexColor('#e74c3c')
COLOR_NEUTRAL = HexColor('#f39c12')
COLOR_GRAY = HexColor('#666666')
COLOR_LIGHT_BG = HexColor('#f5f7fa')


def create_styles():
    """创建 PDF 样式"""
    styles = getSampleStyleSheet()
    font_name = FONT_NAME or 'Helvetica'

    custom_styles = {
        'ReportTitle': ParagraphStyle(
            'ReportTitle',
            fontName=font_name,
            fontSize=22,
            leading=30,
            alignment=TA_CENTER,
            textColor=COLOR_PRIMARY,
            spaceAfter=6 * mm,
        ),
        'ReportMeta': ParagraphStyle(
            'ReportMeta',
            fontName=font_name,
            fontSize=10,
            leading=14,
            alignment=TA_CENTER,
            textColor=COLOR_GRAY,
            spaceAfter=12 * mm,
        ),
        'SectionTitle': ParagraphStyle(
            'SectionTitle',
            fontName=font_name,
            fontSize=16,
            leading=22,
            textColor=COLOR_PRIMARY,
            spaceBefore=10 * mm,
            spaceAfter=5 * mm,
        ),
        'BodyText': ParagraphStyle(
            'BodyText',
            fontName=font_name,
            fontSize=11,
            leading=18,
            textColor=COLOR_SECONDARY,
            spaceAfter=3 * mm,
            alignment=TA_JUSTIFY,
        ),
        'KPIValue': ParagraphStyle(
            'KPIValue',
            fontName=font_name,
            fontSize=24,
            leading=30,
            alignment=TA_CENTER,
            textColor=COLOR_ACCENT,
        ),
        'KPILabel': ParagraphStyle(
            'KPILabel',
            fontName=font_name,
            fontSize=9,
            leading=12,
            alignment=TA_CENTER,
            textColor=COLOR_GRAY,
        ),
        'Disclaimer': ParagraphStyle(
            'Disclaimer',
            fontName=font_name,
            fontSize=8,
            leading=12,
            textColor=COLOR_GRAY,
            alignment=TA_CENTER,
        ),
    }

    for name, style in custom_styles.items():
        styles.add(style)

    return styles


def generate_pdf(output_path, title, period, gen_date, sections):
    """
    生成舆情报告 PDF

    Args:
        output_path: 输出文件路径
        title: 报告标题
        period: 监测周期
        gen_date: 生成日期
        sections: 报告内容章节列表
    """
    registered = register_chinese_font()
    if not registered:
        print("警告: 未能注册中文字体，中文内容可能无法正确显示")

    styles = create_styles()
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
    )

    story = []

    # 报告头部
    story.append(Paragraph(title, styles['ReportTitle']))
    story.append(Paragraph(f"{period} | {gen_date}", styles['ReportMeta']))
    story.append(HRFlowable(width="100%", thickness=1, color=COLOR_ACCENT, spaceAfter=8 * mm))

    # 各章节
    for section in sections:
        story.append(Paragraph(section.get('title', ''), styles['SectionTitle']))
        for content in section.get('content', []):
            story.append(Paragraph(content, styles['BodyText']))

    # 免责声明
    story.append(Spacer(1, 15 * mm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=HexColor('#ddd'), spaceAfter=3 * mm))
    story.append(Paragraph("本报告数据来源于公开网络信息，仅供参考。报告由 AI 自动生成，不代表任何官方立场。", styles['Disclaimer']))

    doc.build(story)
    print(f"PDF 已生成: {output_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='生成舆情报告 PDF')
    parser.add_argument('--output', required=True, help='输出 PDF 文件路径')
    parser.add_argument('--title', default='舆情监测报告', help='报告标题')
    parser.add_argument('--period', default='', help='监测周期')
    parser.add_argument('--date', default='', help='生成日期')
    args = parser.parse_args()

    generate_pdf(args.output, args.title, args.period, args.date, [])
