# pip install google-generativeai
# pip install customtkinter
#pip install pillow

import customtkinter as ctk
import google.generativeai as genai
from PIL import Image

#Configurações da UI



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

janela = ctk.CTk()

janela.geometry("900x800")
janela.resizable(width=False, height=False)

icon_path = "assets/favicon.ico"
janela.iconbitmap(icon_path)

janela.title("Correction-IA")



def api_Google(tema, texto):
    # Configurações do Google api key

    genai.configure(api_key="Cole aqui sua API KEY")

    # Set up the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)



    prompt_parts = [
        "Análise a redação e dê uma nota. Mostre a apenas a nota, pontue em 3 tópicos com comentários mais relevantes sobre a redação e dê um repertório cultural sobre o tema caso o mesmo não tenha. Não esqueça! O texto deve estar de acordo com a redação. Caso contrário, zero. Faça isso apenas com a redação que ainda não tem saída.",

        "Redação Tema: “O estigma associado às doenças mentais na sociedade brasileira” \nTexto:\nNise da Silveira foi uma renomada psiquiatra brasileira que, indo contra a comunidade médica tradicional da sua época, lutou a favor de um tratamento humanizado para pessoas com transtornos psicológicos. No contexto nacional atual, indivíduos com patologias mentais ainda sofrem com diversos estigmas criados. Isso ocorre, pois faltam informações corretas sobre o assunto e, também, existe uma carência de representatividade desse grupo nas mídias. Primariamente, vale ressaltar que a ignorância é uma das principais causas da criação de preconceitos contra portadores de doenças psiquiátricas. Sob essa ótica, o pintor holandês Vincent Van Gogh foi alvo de agressões físicas e psicológicas por sofrer de transtornos neurológicos e não possuir o tratamento adequado. O ocorrido com o artista pode ser presenciado no corpo social brasileiro, visto que, apesar de uma parcela significativa da população lidar com alguma patologia mental, ainda são propagadas informações incorretas sobre o tema. Esse processo fortalece a ideia de que integrantes não são capazes de conviver em sociedade, reforçando estigmas antigos e criando novos. Dessa forma, a ignorância contribui para a estigmatização desses indivíduos e prejudica o coletivo. Ademais, a carência de representatividade nos veículos midiáticos fomenta o preconceito contra pessoas com distúrbios psicológicos. Nesse sentido, a série de televisão da emissora HBO, \"Euphoria\", mostra as dificuldades de conviver com Transtorno Afetivo Bipolar (TAB), ilustrado pela protagonista Rue, que possui a doença. A série é um exemplo de representação desse grupo, nas artes, falando sobre a doença de maneira responsável. Contudo, ainda é pouca a representatividade desses indivíduos em livros, filmes e séries, que quando possuem um papel, muitas vezes, são personagens secundários e não há um aprofundamento de sua história. Desse modo, esse processo agrava os esteriótipos contra essas pessoas e afeta sua autoestima, pois eles não se sentem representados. Portanto, faz-se imprescindível que a mídia - instrumento de ampla abrangência - informe a sociedade a respeito dessas doenças e sobre como conviver com pessoas portadoras, por meio de comerciais periódicos nas redes sociais e debates televisivos, a fim de formar cidadãos informados. Paralelamente, o Estado - principal promotor da harmonia social - deve promover a representatividade de pessoas com transtornos mentais nas artes, por intermédio de incentivos monetários para produzir obras sobre o tema, com o fato de amenizar o problema. Assim, o corpo civil será mais educado e os estigmas contra indivíduos com patologias mentais não serão uma realidade do Brasil.",
        "output: Nota: 1000 pontos",
        "Redação Tema: Invisibilidade e registro civil: garantia de acesso à cidadania no Brasil. \nTexto:\nA questão da invisibilidade social e a falta de registro civil são problemas intrínsecos à realidade brasileira, que comprometem não apenas a identidade individual, mas também o pleno exercício da cidadania. Urge, portanto, uma reflexão sobre como garantir o acesso universal ao registro civil como um direito fundamental para todos os cidadãos. No Brasil contemporâneo, milhões de pessoas vivem à margem do sistema legal devido à ausência de registro civil. Esse fenômeno, frequentemente ligado à pobreza e à falta de acesso a serviços públicos adequados, perpetua um ciclo de exclusão e vulnerabilidade. Sem o registro de nascimento, indivíduos enfrentam obstáculos significativos no acesso a direitos básicos, como educação, saúde e trabalho digno. O registro civil não se limita apenas a um documento burocrático; é um instrumento essencial para a garantia dos direitos fundamentais. Sem ele, indivíduos são privados de sua identidade legal, tornando-se invisíveis aos olhos do Estado e da sociedade. Tal invisibilidade não apenas perpetua a marginalização social, mas também dificulta a implementação de políticas públicas eficazes para combater a pobreza e promover a inclusão social. É imperativo, portanto, adotar medidas concretas para assegurar o acesso universal ao registro civil. Isso inclui campanhas de conscientização sobre a importância do registro desde o nascimento, bem como a facilitação do processo de registro para populações marginalizadas, por meio de políticas públicas inclusivas e acessíveis. Além disso, é fundamental investir em infraestrutura e recursos humanos para garantir a eficiência e a abrangência dos serviços de registro civil em todo o país. Isso envolve a expansão de cartórios e postos de atendimento em áreas remotas e o treinamento de profissionais capacitados para lidar com questões relacionadas ao registro civil. Mais do que uma questão de burocracia, o acesso ao registro civil é uma questão de justiça social e dignidade humana. Garantir que todos os cidadãos brasileiros sejam devidamente registrados é um passo fundamental para promover a inclusão e a cidadania plena no país."
        "output: Nota: 720 pontos",

        "Redação Tema: “Invisibilidade e registro civil: garantia de acesso à cidadania no Brasil”  \nTexto:\nNise da Silveira foi uma renomada psiquiatra brasileira que, indo contra a comunidade médica tradicional da sua época, lutou a favor de um tratamento humanizado para pessoas com transtornos psicológicos. No contexto nacional atual, indivíduos com patologias mentais ainda sofrem com diversos estigmas criados. Isso ocorre, pois faltam informações corretas sobre o assunto e, também, existe uma carência de representatividade desse grupo nas mídias. Primariamente, vale ressaltar que a ignorância é uma das principais causas da criação de preconceitos contra portadores de doenças psiquiátricas. Sob essa ótica, o pintor holandês Vincent Van Gogh foi alvo de agressões físicas e psicológicas por sofrer de transtornos neurológicos e não possuir o tratamento adequado. O ocorrido com o artista pode ser presenciado no corpo social brasileiro, visto que, apesar de uma parcela significativa da população lidar com alguma patologia mental, ainda são propagadas informações incorretas sobre o tema. Esse processo fortalece a ideia de que integrantes não são capazes de conviver em sociedade, reforçando estigmas antigos e criando novos. Dessa forma, a ignorância contribui para a estigmatização desses indivíduos e prejudica o coletivo. Ademais, a carência de representatividade nos veículos midiáticos fomenta o preconceito contra pessoas com distúrbios psicológicos. Nesse sentido, a série de televisão da emissora HBO, \"Euphoria\", mostra as dificuldades de conviver com Transtorno Afetivo Bipolar (TAB), ilustrado pela protagonista Rue, que possui a doença. A série é um exemplo de representação desse grupo, nas artes, falando sobre a doença de maneira responsável. Contudo, ainda é pouca a representatividade desses indivíduos em livros, filmes e séries, que quando possuem um papel, muitas vezes, são personagens secundários e não há um aprofundamento de sua história. Desse modo, esse processo agrava os esteriótipos contra essas pessoas e afeta sua autoestima, pois eles não se sentem representados. Portanto, faz-se imprescindível que a mídia - instrumento de ampla abrangência - informe a sociedade a respeito dessas doenças e sobre como conviver com pessoas portadoras, por meio de comerciais periódicos nas redes sociais e debates televisivos, a fim de formar cidadãos informados. Paralelamente, o Estado - principal promotor da harmonia social - deve promover a representatividade de pessoas com transtornos mentais nas artes, por intermédio de incentivos monetários para produzir obras sobre o tema, com o fato de amenizar o problema. Assim, o corpo civil será mais educado e os estigmas contra indivíduos com patologias mentais não serão uma realidade do Brasil.",

        "output: Nota: 0 ponto, pois não está relacionando o tema e o texto.",
        "Redação Tema: “O estigma associado às doenças mentais na sociedade brasileira” \n\nTexto:\nNo filme estadunidense “Coringa”, o personagem principal, Arthur Fleck, sofre de um transtorno mental que o faz ter episódios de riso exagerado e descontrolado em público, motivo pelo qual é frequentemente atacado nas ruas. Em consonância com a realidade de Arthur, está a de muitos cidadãos, já que o estigma associado às doenças mentais na sociedade brasileira ainda configura um desafio a ser sanado. Isso ocorre, seja pela negligência governamental nesse âmbito, seja pela discriminação desta classe por parcela da população verde-amarela. Dessa maneira, é imperioso que essa chaga social seja resolvida, a fim de que o longa norte-americano não mais reflita o contexto atual da nação. Nessa perspectiva, acerca da lógica referente aos transtornos da mente, é válido retomar o aspecto supracitado quanto à omissão estatal neste caso. Segundo a OMS (Organização Mundial da Saúde), o Brasil é o país que apresenta o maior número de casos de depressão da América Latina e, mesmo diante desse cenário alarmante, os tratamentos às doenças mentais, quando oferecidos, não são, na maioria das vezes, eficazes. Isso acontece pela falta de investimento público em centros especializados no cuidado para com essas condições. Consequentemente, muitos portadores, sobretudo aqueles de menor renda, não são devidamente tratados, contribuindo para sua progressiva marginalização perante o corpo social. Este quadro de inoperância das esferas de poder exemplifica a teoria das Instituições Zumbis, do sociólogo Zygmunt Bauman, que as descreve como presentes na sociedade, mas que não cumprem seu papel com eficácia. Desse modo, é imprescindível que, para a refutação da teoria do estudioso polonês, essa problemática seja revertida.\nParalelamente ao descaso das esferas governamentais nessa questão, é fundamental o debate acerca da aversão de parte dos civis ao grupo em pauta, uma vez que ambos são impasses para sua completa socialização. Esse preconceito se dá pelos errôneos ideais de felicidade disseminados na sociedade como metas universais. Entretanto, essas concepções segregam os indivíduos entre os “fortes” e os “fracos”, em que tais fracos, geralmente, integram a classe em discussão, dado que não atingem essas metas estabelecidas, como a estabilidade emocional. Por conseguinte, aqueles que não alcançam os objetivos são estigmatizados e excluídos do tecido social. Tal conjuntura segregacionista - os que possuem algum tipo de transtorno, nesse caso -- na teia social. Dessa maneira, essa problemática urge ser solucionada para que o princípio da alemã seja validado no país tupiniquim.Portanto, são essenciais medidas operantes para a reversão do estigma associado às doenças mentais na sociedade brasileira. Para isso, compete ao Ministério da Saúde investir na melhora da qualidade dos tratamentos a essas doenças nos centros públicos especializados de cuidados, destinando mais medicamentos e contratando, por concursos, mais profissionais da área, como psiquiatras e enfermeiros. Isso deve ser feito por meio de recursos autorizados pelo Tribunal de Contas da União - órgão que opera feitos públicos - com o fito de potencializar o atendimento a esses pacientes e oferecê-los um tratamento eficaz. Ademais, palestras devem ser realizadas em espaços públicos sobre os malefícios das falsas concepções de prazer e da importância do acolhimento dos vulneráveis. Assim, os ideais inalcançáveis não mais serão instrumentos segregadores e, finalmente, a cotação de Fleck não mais representará a dos brasileiros.",
        "output: Nota: 1000 pontos",
        "Redação Tema: 'Desafios para o enfrentamento da invisibilidade do trabalho de cuidado realizado pela mulher no Brasil'\n\nTexto:\nDe acordo com a pensadora brasileira Djamila Ribeiro, o primeiro passo a ser tomado para solucionar uma questão é tirá-la da invisibilidade. Porém, no contexto atual do Brasil, as mulheres enfrentam diversos desafios para que seu trabalho de cuidado seja reconhecido, gerando graves impactos em suas vidas, como a falta de destaque. Nesse sentido, essa problemática ocorre em virtude da omissão governamental e da influência midiática. Dessa forma, em primeiro plano, é preciso atentar para o descaso estatal em relação aos obstáculos enfrentados diariamente por mulheres que trabalham como cuidadoras. Segundo John Locke, “as leis fizeram-se para os homens e não para as leis”. No entanto, a inércia governamental direcionada à tais pessoas não cumpre com o previsto na Carta Magna, visto que a falta de investimento em políticas públicas causa dificuldades no âmbito profissional deste setor - como a desvalorização salarial. Isso contribui para que suas necessidades sejam cada vez mais negligenciadas. Além disso, a influência dos meios digitais é um fator agravante no que tange ao problema. Para Chimamanda Adichie, mudar o “status quo” - o estado atual das coisas - é sempre penoso. Essa conjuntura pode ser observada no papel que a mídia possui na luta diária de mulheres que exercem o trabalho do cuidado ou doméstico, uma vez que ela auxilia no fortalecimento de uma mentalidade social machista no país. Isso ocasionou o silenciamento da população feminina, enraizando a lógica do patriarcado na sociedade. Diante do exposto, as mulheres perdem a voz na busca por direitos profissionais na área de cuidado, ao ser propagada a ideia de que essa função é sua, e somente sua, obrigação.Portanto, é necessário que esta situação seja dissolvida. Para isso, o governo, órgão responsável por garantir a condição e existência de todos, deve prover apoio psicológico e financeiro às cuidadoras, por meio de investimentos e pelo exercício das leis, a fim de sanar a vulnerabilidade socioeconômica existente no cotidiano desses grupos. Paralelamente, os meios de comunicação precisam combater a lógica de inferioridade e a concepção machista agregadas a este trabalho. Assim, será possível solucionar esta questão, pois será retirada do cenário de invisibilidade, como propõe Djamila.",
        "output: Nota: 1000 pontos",
        "Redação Tema: 'Desafios para o enfrentamento da invisibilidade do trabalho de cuidado realizado pela mulher no Brasil'\n\nTexto:\nA Constituição Federal de 1988, documento jurídico mais importante do país, garante o trabalho remunerado e a dignidade humana como direitos de todo cidadão brasileiro, além de estabelecer a igualdade entre os gêneros masculino e feminino na sociedade. Entretanto, nota-se que tal prerrogativa não tem se reverberado na prática, visto que ainda há uma invisibilidade do trabalho de cuidado realizado pela mulher no Brasil, o qual, muitas vezes, não apresenta retorno financeiro. Portanto, faz-se necessária a análise dos principais fatores que contribuem para esse triste cenário: o machismo e o descaso estatal.Em primeira análise, é importante destacar que a mulher ocupa uma posição subjugada na sociedade brasileira desde o período colonial, sendo encarregada dos afazeres domésticos e dos cuidados familiares. A partir desse contexto, após anos de inferiorização, as mulheres conquistaram diversos direitos sociopolíticos, como o direito ao voto e o trabalho remunerado. Todavia, mesmo com essas conquistas, ainda é notável que existe um machismo estrutural na sociedade contemporânea, já que, segundo o IBGE, as mulheres gastam o dobro de tempo com tarefas de cuidado, quando comparadas aos homens. Nesse sentido, por ser uma tradição enraizada na sociedade, o trabalho de cuidado realizado pela população feminina é ignorado por grande parte das pessoas.Ademais, é imperioso ressaltar que a invisibilidade e a desvalorização desse tipo de trabalho resultam, em alguns casos, na falta de remuneração, o que contraria o direito estabelecido na Constituição. De acordo com o filósofo Nicolau Maquiagem, o principal objetivo do governante é a manutenção do poder, deixando em segundo plano a busca pelo bem comum. Assim, é evidente que o Estado não se preocupa com a garantia dos direitos das mulheres, o que reflete na ausência de políticas públicas que assegurem uma remuneração digna àquelas que trabalham. dessa forma, as mulheres se encontram desamparadas, ao mesmo tempo, pela sociedade e pelo governo. Portanto, é necessário promover ações concretas, as quais alterem o quadro de invisibilidade do trabalho realizado pela população feminina. Logo, cabe às emissoras de TV, as quais são grandes formadoras de opinião da sociedade, realizar campanhas sobre a importância de lutar contra o machismo, por meio de anúncios publicitários, a fim de desconstruir ideias de subjugação presentes no Brasil contemporâneo. Além disso, o Governo Federal deve fiscalizar as relações de trabalho para garantir a remuneração feminina.",
        "output: Nota: 1000 pontos",
        "Redação Tema:\n“Invisibilidade e registro civil: garantia de acesso à cidadania no Brasil”\n\nTexto:\nA Constituição Federal de 1988, assegura uma série de direitos a todos os cidadãos. Contudo, nem todos conseguem usufruir destes direitos. Segundo o IBGE, cerca de 2,94 milhões de brasileiros não possuem registro de nascimento, o que os caracteriza como invisíveis aos olhos do Estado. A manutenção deste cenário se sustenta devido à posição geográfica e a negligência estatal. Sendo assim, ações devem ser efetivadas para romper com essa situação.\n\nSob esse viés, vale destacar que o Brasil tem um território muito extenso e isso dificulta a sua chegada governamental a todos. Diversas pessoas residem longe de centros urbanos e a viagem até o cartório, muitas vezes, não compensa, visto que, a confecção do documento não traz os serviços estatais, como a escola, para perto das suas casas.\n\nOutrossim, seguindo a perspectiva de John Locke, o Estado como promotor do bem-estar coletivo, não pode esquivar-se da responsabilidade de fornecer direitos à toda a população. Porém, para isso, ele precisa visualizá-la por completo. Logo, parte dele solucionar o problema de registro civil.\n\nPortanto, para mitigar a invisibilidade civil e potencializar o acesso aos direitos, o Governo Federal por meio de políticas públicas, deve espalhar-se melhor por todo o território brasileiro. Com o nome \"Direito a todos\", esta política terá como finalidade o espalhamento dos veículos estatais pelo país. Com isso, o Brasil se tornará um país que garante a ampla defesa dos direitos fundamentais a seus cidadãos",
        "output: Nota: 800 pontos",
        "Redação Tema: 'Desafios para o enfrentamento da invisibilidade do trabalho de cuidado realizado pela mulher no Brasil'\n\nTexto:\nSegundo o IBGE, as mulheres têm mais que o dobro de horas trabalhadas em relação aos homens. Isso acontece porque muitas mulheres precisam realizar tarefas domésticas, antes ou depois da jornada de trabalho remunerada. Embora serem necessárias, essas tarefas são constamente desvalorizadas e ignoradas. Desse modo, a manutenção deste problema configura o dessegmento da Constituição Federal de 1988, onde assegura-se a igualdade de gênero.\n\nSob esse viés, é válido destacar que o machismo estrutural é um dos principais responsáveis da invisibilidade do trabalho de cuidado realizado pelas mulheres. O filme da \"Barbie\", sucesso de bilheteria, evidencia que desde o nascimento, as mulheres são designadas a cuidar de crianças. Desta forma, a responsabilidade do lar é imposta somente ao gênero feminino.\n\nOutrossim, segundo a visão de John Locke, o Estado é responsável pelo bem-estar social. Porém, o mesmo não se mobiliza de tomar as devidas ações para solucionar o problema. A falta de medidas intervencionistas qualifica a administração governamental como negligente.\n\nEm suma, a invisibilidade do trabalho de cuidado só será combatida com a superação dos estigmas que prendem o gênero feminino. A melhor arma contra o preconceito é a educação. Isso porque, segundo Immanuel Kant, é ela que forma o indivíduo. Portanto, o Governo Federal por meio do Ministério da Educação, deve acrescentar a matéria de sociologia desde a base do desenvolvimento infantil. Apenas assim que as responsabilidades do lar serão entendidas como universais pelos estudantes. Desse modo, o Brasil se tornará um país que garante a ampla defesa dos direitos fundamentais a seus cidadãos.",
        "output: Nota: 820",
        "Redação Tema: " + tema + texto,
        "output: ",
    ]

    response = model.generate_content(prompt_parts)
    resposta = str(response.text)
    resposta = resposta.replace("*", "-")
    caixa_resposta.delete("0.0", "end")
    caixa_resposta.insert("0.0", resposta)


def enviar():
    tema = str(caixa_tema.get())
    texto = caixa_texto.get("1.0", "end-1c")
    if (tema != "" and texto != "") :
        api_Google(tema, texto)


caixa_tema = ctk.CTkEntry(janela,  width=300, placeholder_text="Digite o tema aqui")
caixa_tema.place(relx=0.5, rely=0.21, anchor=ctk.CENTER)


#Imagem:
my_img = ctk.CTkImage(light_image=Image.open('assets/Correction-ia-title.png'), size=(210, 120))
my_label = ctk.CTkLabel(janela, text="", image=my_img)
my_label.place(relx=0.5, rely=0.10, anchor=ctk.CENTER)
my_label.pack(padx=10, pady=15)


# Crie uma caixa de texto
caixa_texto = ctk.CTkTextbox(janela, width=400,  corner_radius=10, border_width=0, )
caixa_texto.insert("0.0", "Digite sua redação aqui")
caixa_texto.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

# Análise:
caixa_resposta = ctk.CTkTextbox(janela, width=400, corner_radius=10, border_width=0,)
caixa_resposta.insert("0.0", "Sua análise estará aqui")
caixa_resposta.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)




#Cria um botao:
botao = ctk.CTkButton(janela, width=50, text="Enviar", command=enviar)
botao.place(relx=0.75, rely=0.21, anchor=ctk.CENTER)

janela.mainloop()
