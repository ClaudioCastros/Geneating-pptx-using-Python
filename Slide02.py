############## SLIDE 2
def slide02(prs, slide_de_titulo):
    slide = prs.slides.add_slide(slide_de_titulo)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]

    title.text = "Hello, World!"
    subtitle.text = "python-pptx was here!"