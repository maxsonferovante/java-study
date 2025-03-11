import os
import shutil
import datetime

def normalize_filenames():
    # Listar todos os livros
    book_dir = 'books'
    list_of_files = os.listdir(book_dir)
    
    for file in list_of_files:
        # Normalizar o nome do arquivo (substituir espaços por underscores)
        normalized_name = file.replace(' ', '_')
        normalized_name = normalized_name.replace('(', '')
        normalized_name = normalized_name.replace(')', '')
        normalized_name = normalized_name.replace(',', '')
        normalized_name = normalized_name.replace(';', '')
        normalized_name = normalized_name.replace('!', '')

        
        # Caminho completo dos arquivos
        old_path = os.path.join(book_dir, file)
        new_path = os.path.join(book_dir, normalized_name)
            
            # Renomear o arquivo
        shutil.move(old_path, new_path)
        print(f"Arquivo renomeado: '{file}' -> '{normalized_name}'")

def generate_readme():
    # Cabeçalho do README
    readme_content = "# Java Study\n\n"
    readme_content += "Este repositório contém recursos de estudo relacionados a Java e tecnologias associadas.\n\n"
    # Adicionar um badge para a ação de atualização automática do README

    readme_content += "[![Atualização automática do README](https://github.com/maxsonferovante/java-study/actions/workflows/main.yml/badge.svg?event=workflow_dispatch)](https://github.com/maxsonferovante/java-study/actions/workflows/main.yml)\n\n"
    # Adicionar seção de livros
    readme_content += "## Livros Disponíveis\n\n"
    
    # Listar todos os livros
    list_of_files = sorted(os.listdir('books'))
    
    for index, file in enumerate(list_of_files):
        # Remover a extensão .pdf para uma apresentação mais limpa
        book_name = file
        if book_name.lower().endswith('.pdf'):
            book_name = book_name[:-4]
        
        # Substituir underscores por espaços para exibição mais amigável
        display_name = book_name.replace('_', ' ')
        
        date_modified = os.path.getmtime(f'books/{file}')        
        date_modified = datetime.datetime.fromtimestamp(date_modified)
        date_modified = date_modified.strftime('%d/%m/%Y')

        # Criar um link para o arquivo PDF usando sintaxe Markdown com uma numeração e data de modificação
        readme_content += f"{index+1}. [{display_name}](books/{file}) - {date_modified}\n"

    

    # Adicionar uma seção de contribuição
    readme_content += "\n## Contribuição\n\n"
    readme_content += "Contribuições são bem-vindas! Para contribuir, siga os passos abaixo:\n\n"
    readme_content += "1. Faça um fork deste repositório\n"
    readme_content += "2. Crie uma branch com a sua feature: `git checkout -b minha-feature`\n"
    readme_content += "3. Faça commit das suas mudanças: `git commit -m 'Adiciona minha feature'`\n"
    readme_content += "4. Faça push para a sua branch: `git push origin minha-feature`\n"
    readme_content += "5. Abra um Pull Request\n\n"

    
    # Escrever o conteúdo no arquivo README.md
    with open('README.md', 'w') as readme_file:
        readme_file.write(readme_content)
    
    print("README.md foi gerado com sucesso!")

if __name__ == "__main__":
    # Primeiro normalizar os nomes dos arquivos
    normalize_filenames()
    # Depois gerar o README
    generate_readme()
