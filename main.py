# This is a sample Python script.
import json

from LLM import LLM
import gradio as gr


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def process(ticket):
    llm = LLM()
    output = llm.analyze_ticket(ticket).choices[0].message.content
    print(output)
    result = json.loads(output)
    return result['queue'], result['priority']

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # print(llm.create_chat_completion('Was gibt es in Darmstadt zu besichtigen?').choices[0].message.content)

    demo = gr.Interface(
        process,
        [
            gr.TextArea(
                label="Tickettext"
            ),
        ],
        [
            gr.Radio(
                ["netz", "software", "raumbuchung", "multimedia"],
                label="Ticket-Queue"
            ),
            gr.Radio(
                ["sehr dringend", "dringend", "weniger dringend"],
                label="Priorität"
            )
        ],
        #examples=[
        #    [45, "add", 3],
        #    [3.14, "divide", 2],
        #    [144, "multiply", 2.5],
        #    [0, "subtract", 1.2],
        #],
        title="Ticket-Vorverarbeitung",
        description="Analysiert das eingegebene Ticket und kategorisiert den Inhalt.",
    )

    demo.launch(server_port=7860, share=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
