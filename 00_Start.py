#####################################################################
#              Apresentações PowerPoint com Python                  #
#####################################################################
# Auto: Claudio Castro                                              #
# Ref.: python-pptx.readthedocs.io/en/latest/index.html             #
# Ref.: hashtagtreinamentos.com/integracao-powerpoint-python        #
# Data: 08/10/2022                                                  #
# Versão: 1.0.0                                                     #
# Last Update:                                                      #
#####################################################################

#Required libs: pip install python-pptx
#####################################################################

# PARTE 3
import collections.abc
from pptx import Presentation


#abrindo uma apresentação existente
prs = Presentation('Geneating pptx using Python\\templates\\template.pptx')

################################################
#                # Templates #                 #
################################################
slide_de_titulo = prs.slide_layouts[0]         #
slide_e_conteudo = prs.slide_layouts[1]        #
cabecalho_da_sessao = prs.slide_layouts[2]     #
duas_partes_de_conteudo = prs.slide_layouts[3] #
comparacao = prs.slide_layouts[4]              #
somente_titulo = prs.slide_layouts[5]          #
em_branco = prs.slide_layouts[6]               #
conteudo_com_legenda = prs.slide_layouts[7]    #
imagem_com_legenda = prs.slide_layouts[8]      #
################################################

from Slide01 import slide01
from Slide02 import slide02
from Slide03 import slide03
from Slide04 import slide04
from Slide05 import slide05
from Slide06 import slide06
from Slide07 import slide07

# trabalhando cada slide
slide01(prs)
slide02(prs, slide_de_titulo)
slide03(prs, slide_e_conteudo)
slide04(prs, em_branco)
slide05(prs, em_branco)
slide06(prs, somente_titulo)
slide07(prs, somente_titulo)

############## END
prs.save('output.pptx')