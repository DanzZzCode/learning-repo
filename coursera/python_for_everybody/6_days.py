import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def create_workout_pdf(filename="3_Day_Full_Body_Illustrated_Blueprint.pdf"):
    # Target page layout setup
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=40, leftMargin=40,
        topMargin=40, bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Palette
    PRIMARY_COLOR = colors.HexColor("#1A2B4C")    # Deep Navy
    SECONDARY_COLOR = colors.HexColor("#2E5B88")  # Slate Blue
    TEXT_COLOR = colors.HexColor("#2C3E50")       # Charcoal Body Text
    ACCENT_COLOR = colors.HexColor("#E74C3C")     # Accent Coral
    BG_LIGHT = colors.HexColor("#F8F9FA")         # Off-white panel
    
    # Custom Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=PRIMARY_COLOR,
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=SECONDARY_COLOR,
        spaceAfter=15
    )
    
    h1_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=PRIMARY_COLOR,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=TEXT_COLOR
    )
    
    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12,
        textColor=colors.white,
        alignment=1
    )
    
    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=TEXT_COLOR
    )

    story = []
    
    # Header Section
    story.append(Paragraph("3-Day Home Full-Body Blueprint", title_style))
    story.append(Paragraph("Physique Conditioning & Strength Foundation Program | Height: 188 cm | Weight: 70 kg", subtitle_style))
    
    # Schedule Grid Text
    story.append(Paragraph("Weekly Schedule Grid", h1_style))
    
    sched_data = [
        [Paragraph("Day", table_header_style), Paragraph("Status", table_header_style), Paragraph("Focus Split", table_header_style), Paragraph("Primary Targets", table_header_style)],
        [Paragraph("<b>Saturday</b>", table_cell_style), Paragraph("WORKOUT", table_cell_style), Paragraph("Workout A (Push & Lower Focus)", table_cell_style), Paragraph("Chest, Back, Quads, Glutes, Core", table_cell_style)],
        [Paragraph("Sunday", table_cell_style), Paragraph("Rest", table_cell_style), Paragraph("Full System Recovery", table_cell_style), Paragraph("CNS Recharge & Fuel Absorption", table_cell_style)],
        [Paragraph("<b>Monday</b>", table_cell_style), Paragraph("WORKOUT", table_cell_style), Paragraph("Workout B (Pull & Core Focus)", table_cell_style), Paragraph("Back, Shoulders, Legs, Core Stability", table_cell_style)],
        [Paragraph("Tuesday", table_cell_style), Paragraph("Rest", table_cell_style), Paragraph("Full System Recovery", table_cell_style), Paragraph("CNS Recharge & Joint Relief", table_cell_style)],
        [Paragraph("<b>Wednesday</b>", table_cell_style), Paragraph("WORKOUT", table_cell_style), Paragraph("Workout A (Push & Lower Focus)", table_cell_style), Paragraph("Chest, Back, Quads, Glutes, Core", table_cell_style)],
        [Paragraph("Thursday", table_cell_style), Paragraph("Rest", table_cell_style), Paragraph("Full System Recovery", table_cell_style), Paragraph("Muscular Repair & Growth Window", table_cell_style)],
        [Paragraph("Friday", table_cell_style), Paragraph("Rest", table_cell_style), Paragraph("Full System Recovery", table_cell_style), Paragraph("Deep System Reset for Saturday", table_cell_style)]
    ]
    
    sched_table = Table(sched_data, colWidths=[70, 75, 175, 212])
    sched_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), SECONDARY_COLOR),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#BDC3C7")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, BG_LIGHT])
    ]))
    story.append(sched_table)
    story.append(Spacer(1, 15))
    
    # Function to build uniform tables for exercise breakdowns
    def generate_exercise_panel(name, volume, execution):
        panel_data = [
            [Paragraph(f"<b>{name}</b>", ParagraphStyle('ExTitle', parent=h1_style, textColor=colors.white, spaceBefore=0, spaceAfter=0)), 
             Paragraph(f"<b>Volume:</b> {volume}", ParagraphStyle('ExVol', parent=body_style, textColor=colors.white, fontName='Helvetica-Bold'))],
            [Paragraph(f"<b>Execution Plan:</b> {execution}", body_style), ""]
        ]
        panel_table = Table(panel_data, colWidths=[270, 262])
        panel_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), PRIMARY_COLOR),
            ('SPAN', (0,1), (1,1)),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
            ('BOX', (0,0), (-1,-1), 1, SECONDARY_COLOR),
            ('BACKGROUND', (0,1), (-1,-1), BG_LIGHT),
        ]))
        return panel_table

    # --- WORKOUT A SECTION ---
    story.append(Paragraph("1. Workout A: Push & Lower Body Focus (Saturday / Wednesday)", h1_style))
    story.append(Spacer(1, 4))
    
    story.append(generate_exercise_panel(
        "Standard Push-Ups", "3 Sets x 10-15 Reps",
        "Keep your body in a perfectly straight line from head to heels. Control the lowering phase strictly (2-3 seconds). Keep elbows tucked at a 45-degree angle from your ribs to protect shoulder joints."
    ))
    story.append(Spacer(1, 8))
    
    story.append(generate_exercise_panel(
        "Door Frame Rows", "3 Sets x 12-15 Reps",
        "Grip the outer door frame firmly with your fingers. Place your feet close to the base of the wall, lean back until your arms are straight, and pull your chest smoothly toward the wood panel. Keep shoulders packed down."
    ))
    story.append(Spacer(1, 8))
    
    story.append(generate_exercise_panel(
        "Bulgarian Split Squats", "3 Sets x 10-12 Reps / leg",
        "Stand about two feet in front of a standard chair and rest the top of your rear foot on the seat. Keep your torso completely upright, drop your back knee down cleanly, and drive weight vertically through your front heel."
    ))
    story.append(Spacer(1, 8))
    
    story.append(generate_exercise_panel(
        "Plank to Body Saw", "3 Sets x 45 Seconds",
        "Maintain a rigid low elbow plank with abs compressed. Rock your entire body weight forward and backward smoothly using only your ankles. Do not let your hips sag toward the floor."
    ))
    
    story.append(Spacer(1, 15))
    
    # --- WORKOUT B SECTION ---
    story.append(Paragraph("2. Workout B: Pull & Core Focus (Monday)", h1_style))
    story.append(Spacer(1, 4))
    
    story.append(generate_exercise_panel(
        "Towel Bodyweight Rows", "3 Sets x 8-12 Reps",
        "Securely knot a long towel over the top of a closed door. Grab the towel ends tightly, walk your feet forward toward the door base, lean back, and use an intense grip to smoothly pull your chest up to your hands."
    ))
    story.append(Spacer(1, 8))
    
    story.append(generate_exercise_panel(
        "Pike Push-Ups", "3 Sets x 6-10 Reps",
        "Walk feet toward hands, keeping legs straight and sending your hips high in the air to form an inverted 'V'. Lower the top of your head forward of your hands under full control, then drive straight back up."
    ))
    story.append(Spacer(1, 8))
    
    story.append(generate_exercise_panel(
        "Tempo Bodyweight Squats", "3 Sets x 15-20 Reps",
        "Stand feet shoulder-width apart. Enforce a strict 3-second lowering tempo down to a deep parallel squat position. Pause for 1 second at the absolute bottom, then explode straight upward."
    ))
    story.append(Spacer(1, 8))
    
    story.append(generate_exercise_panel(
        "Bicep Isometric Hold", "3 Sets x 20 Second Hold",
        "Stand squarely on a long towel. Grip the ends tightly with elbows bent at a strict 90-degree angle. Pull upward on the towel with maximum voluntary effort for the entire 20 seconds to trigger deep neural recruitment."
    ))
    story.append(Spacer(1, 8))
    
    story.append(generate_exercise_panel(
        "Reverse Crunches", "3 Sets x 12-15 Reps",
        "Lie completely flat on your back with hands at sides. Tilt your pelvis backward and use your lower core muscles to lift your tailbone smoothly off the floor. Lower your legs slowly under full control."
    ))
    
    story.append(Spacer(1, 15))
    
    # --- STRATEGIC DIRECTIVES ---
    story.append(Paragraph("3. Core Execution Protocol", h1_style))
    directives = (
        "<b>Systemic Recovery Windows:</b> On your designated off days (Sunday, Tuesday, Thursday, Friday), perform no structured training. Allow your nervous system to fully recharge and clear metabolic fatigue.<br/><br/>"
        "<b>Nutritional Strategy Alignment:</b> Consume your 25mg zinc gluconate immediately following your whole-food lunch to protect your stomach. Maintain a consistent 3 to 3.5 liters of water daily to support digestion as you scale up your roasted soybean and oat fiber intake."
    )
    story.append(Paragraph(directives, body_style))

    doc.build(story)

if __name__ == "__main__":
    create_workout_pdf()