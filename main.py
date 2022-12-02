import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

def listen_comand():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return 'Dammm.....Ничего не понял'

def greeting():
    return "Приветствую Босс"

def todo_task():
    print("Что добавим в список дел,Босс?")
    query = listen_comand()
    with open('todo_task.txt','a') as file:
        file.write(f'{query}\n')

    return f"Задача {query} записана"

def main():
    query = listen_comand()
    if query == "запуск":
        print(greeting())
    elif query == "задача":
        print(todo_task())
    else:
        print(query)

if __name__ == "__main__":
    main()