import openai
import config
import typer
from rich import print
from rich.table import Table

def main():
    openai.api_key = config.api_key

    #Saludo
    print("[bold green]ChatGPT API en Python[/bold green]")

    #Creacion de la tabla de informacion
    table = Table("Comando", "Descripcion")
    table.add_row("exit", "Salir de la aplicacion")
    table.add_row("new", "Crear una nueva conversacion")

    print(table)

    #Contexto del asistente 
    context = {"role": "system",
               "content": "Eres un asistente muy útil."}
    messages = [context]

    #Insercion de preguntas
    while True:
        content = __prompt()

        if content == "new":
            print("Nueva conversacion creada")
            messages =[context]
            content = __prompt()

        messages.append({"role":"user", "content":content})

        response =openai.ChatCompletion.create(
            model="gpt-3.5-turbo",messages=messages)
        
        #Opcion para guardar la respuesta 
        response_content = response.choices[0].message.content 
        messages.append({"role":"assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")

#Funcion de confirmacion de salir del sistema
def __prompt() -> str:
    prompt = typer.prompt("\n¿Cual es tu pregunta de hoy?")

    if prompt == "exit":
        exit =typer.confirm("¿Estas seguro?")
        if exit:
            print("¡Hasta luego!")
            raise typer.Abort()
        return __prompt()
    return prompt

if __name__ == "__main__":
    typer.run(main)