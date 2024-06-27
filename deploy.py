# Execute este script para fazer o Deploy das alterações no GitHub
import os

# Gerar índice de entrevistas
interviewsFolder = "./docs/entrevistas"

interviewList = os.listdir(interviewsFolder)
interviewList.remove("index.md")

interviewName = []

for i in interviewList:
    interviewName.append(i.replace("-", " ").removesuffix(".md").title())

newIndex = "# Entrevistas Catalogadas\n\n"

for i in range(len(interviewList)):
    newIndex += f"#### [{interviewName[i]}]({interviewList[i]})\n\n"

# Aplicar novo índice
indexFile = open(interviewsFolder + "/index.md", "w")
indexFile.write(newIndex)
indexFile.close

# Buildar nova versão estática do site
os.system("mkdocs build")

# Relatório final
print("""
=== ORIENTAÇÕES ===
Suba os arquivos da pasta no GitHub para fazer o deploy.
Se estiver devidamente configurado, serão os seguintes comandos:
      
    git add .
    git commit -m "Atualização da documentação"
    git push
""")