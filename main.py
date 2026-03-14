import threading
import time
from agent import handle_user_message

def main():
    print("Assistente meteorológico iniciado. Digite 'sair' para encerrar.")

    while True:
        user_message = input("\nVocê: ").strip()

        if user_message.lower() in {"sair", "exit", "quit"}:
            print("Encerrando assistente.")
            break

        if not user_message:
            print("Digite uma pergunta.")
            continue

        stop_event = threading.Event()

        animation_thread = threading.Thread(
            target=thinking_animation, args=(stop_event,)
        )
        animation_thread.start()

        try:
            response = handle_user_message(user_message)
        finally:
            stop_event.set()
            animation_thread.join()

        print("\r" + " " * 40, end="\r")  
        print(f"Assistente:\n{response}")



def thinking_animation(stop_event):
    dots = ""

    while not stop_event.is_set():
        dots = "." if dots == "..." else dots + "."
        print(f"\rpensando{dots}   ", end="", flush=True)
        time.sleep(0.5)


if __name__ == "__main__":
    main()