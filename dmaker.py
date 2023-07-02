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
<!DOCTYPE html>
<html>
<head>
    <title>{titulo}</title>
    <style>
        body {{
            background-image: url({background});
            color: {cor_texto};
            font-style: {estilo_texto};
            font-family: {fonte};
            background-color: {cor_fundo};
        }}
    </style>
</head>
<body>
    <h1>{titulo}</h1>
    <p>Autor: {autor}</p>
    <img src="{imagem}" alt="Imagem" />
    <div>{conteudo}</div>
    <p>Contato: {contato_anonimo}</p>
    <audio controls>
        <source src="{musica}" type="audio/mpeg">
    </audio>
</body>
</html>
'''

# Define o nome do arquivo de saída
nome_arquivo = input("Digite o nome do arquivo de saída: ")

# Salva o conteúdo HTML no arquivo
with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(html)

print(f"Página criada com sucesso. O arquivo {nome_arquivo} foi gerado.")
