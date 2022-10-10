
########### Slide 1
def slide01(prs):
    for slide in prs.slides:
        slide.shapes[0].text = "Certificado de Participação"
        slide.shapes[1].text = "Certifica-se que Claudio Castro, de idade 25, do curso Ciências da Computação esteve presente nas jornadas de programação python."