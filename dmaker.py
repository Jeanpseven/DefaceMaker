# Solicita informações do usuário
titulo = input("Digite o título da página: ")
conteudo = input("Digite o conteúdo da página: ")
autor = input("Digite o nome do autor: ")
background = input("Digite o caminho para a imagem de fundo (deixe em branco para não usar): ")
musica = input("Digite o caminho para o arquivo de música (deixe em branco para não usar): ")
imagem = input("Digite o caminho para a imagem acima do texto (deixe em branco para não usar): ")
cor_texto = input("Digite a cor do texto (em hexadecimal ou nome da cor): ")
estilo_texto = input("Digite o estilo do texto (por exemplo, 'bold', 'italic', 'underline'): ")
fonte = input("Digite o nome da fonte (por exemplo, 'Arial', 'Verdana'): ")
cor_fundo = input("Digite a cor de fundo da página (em hexadecimal ou nome da cor): ")
contato_anonimo = input("Digite a informação de contato anônimo: ")
mensagem = input("Digite a mensagem a ser deixada na pagina: ")

# Converte nomes de cores em códigos hexadecimais
cores = {
    'preto': '#000000',
    'branco': '#FFFFFF',
    'vermelho': '#FF0000',
    'verde': '#00FF00',
    'azul': '#0000FF',
    'amarelo': '#FFFF00',
    'roxo': '#800080',
    'laranja': '#FFA500',
    'cinza': '#808080',
    'rosa': '#FFC0CB',
    'marrom': '#A52A2A',
    'turquesa': '#40E0D0',
    # Adicione outras cores aqui
}

if cor_texto.lower() in cores:
    cor_texto = cores[cor_texto.lower()]

if cor_fundo.lower() in cores:
    cor_fundo = cores[cor_fundo.lower()]

# Cria o conteúdo HTML da página
html = f'''
<!-- Generator by Nathan Prinsley - https://script-deface-generator.prinsh.com -->
<!DOCTYPE html>
<html>
<head>
    <title>{titulo}</title>
    <meta charset="UTF-8"/>
    <meta name="author" content="{autor}"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <meta name="description" content=""/>
    <meta property="og:title" content="{titulo}"/>
    <meta name="keywords" content="{titulo}"/>
    <meta property="og:image" content="{imagem}"/>
    <meta property="og:type" content="website"/>
    <meta property="og:site_name" content="Haxor Uploader"/>
    <link rel="shortcut icon" type="image/x-icon" href="{imagem}" />
    <link rel="stylesheet" type="text/css" href="https://cdn.prinsh.com/NathanPrinsley-textstyle/nprinsh-stext.css"/>
    <style>
        body {{
            background: {cor_fundo};
            font-family: {fonte};
            margin-top: 35px;
        }}
        h1, h2 {{
            margin-top: .3em;
            margin-bottom: .3em;
        }}
        h1.nprinsleyy {{
            color: #dbd9d9;
            font-size: 32px;
        }}
        h2 {{
            color: #dbd9d9;
            font-size: 10px;
        }}
        p.message_prinsley {{
            color: #dbd9d9;
            margin-top: .25em;
            margin-bottom: .25em;
            font-size: 16px;
            font-weight: unset;
        }}
        .hubungi_prinsh {{
            color: #00eb00;
            text-decoration: none;
        }}
        .hubungi_prinsh:hover {{
            color: red;
        }}
        .othermes_nprinsh {{
            color: #dbd9d9;
            font-size: 16px;
        }}
        marquee.foonathanPrinsley {{
            display: none;
            position: fixed;
            width: 100%;
            bottom: 0px;
            font-family: Tahoma;
            height: 20px;
            color: white;
            left: 0px;
            border-top: 2px solid darkred;
            padding: 5px;
            background-color: #000;
        }}
    </style>
</head>
<body>
    <center>
        <img src="{imagem}" style="width: 20%">
        <h1 class="nprinsleyy nprinsley-text-rainbowan">{titulo}</h1>
        <h2>{autor}</h2>
        <p class="message_prinsley">{mensagem}</p>
        <p style="font-size: 20px;"><a class="hubungi_prinsh" href="mailto:">negociações em pplayboyyhacker@gmail.com</a></p>
        <audio src="{musica}" autoplay="1" loop="1"></audio>
        <marquee class="foonathanPrinsley"><b style="color: #dbd9d9; font-size: 16px;"></b></marquee>
    </center>
</body>
</html>
'''

# Define o nome do arquivo de saída
nome_arquivo = input("Digite o nome do arquivo de saída: ")

# Salva o conteúdo HTML no arquivo
with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(html)

print(f"Página criada com sucesso. O arquivo {nome_arquivo} foi gerado.")
