import gradio as gr
import json
from LLM import LLM

def process(ticket):
    llm = LLM()
    output = llm.analyze_ticket(ticket).choices[0].message.content
    print(output)
    result = json.loads(output)
    return result['queue'], result['priority']

def altes_layout():
    demo = gr.Interface(
        process,
        [
            gr.Text(
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
    title="Ticket-Vorverarbeitung",
       description="Analysiert das eingegebene Ticket und kategorisiert den Inhalt.",
    )
    return demo

def neues_layout():
    with gr.Blocks() as demo:
        with gr.Row():
            gr.Label('Ticket-Vorverarbeitung', label='')
        with gr.Row():
            with gr.Column(scale=1, min_width=300):
                tickettext = gr.TextArea(
                    label="Tickettext"
                )
            with gr.Column(scale=1, min_width=300):
                with gr.Row():
                    with gr.Column(scale=1, min_width=300):
                        queue = gr.Radio(
                            ["netz", "software", "raumbuchung", "multimedia"],
                            label="Ticket-Queue"
                        )
                with gr.Row():
                    with gr.Column(scale=1, min_width=300):
                        priority = gr.Radio(
                            ["sehr dringend", "dringend", "weniger dringend"],
                            label="Priorität"
                        )

        with gr.Row():
            greet_btn = gr.Button("Analysieren")
            greet_btn.click(
                fn=process,
                inputs=[tickettext],
                outputs=[queue, priority]
            )

    return demo

if __name__ == '__main__':
    # demo = altes_layout()
    demo = neues_layout()

    demo.launch(server_port=7860, share=True)
