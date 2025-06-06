import random

def main():
    print("🇹🇷 Welcome to the Turkish Vocabulary Quiz! 🎉")
    print("You'll be asked to translate Turkish words into English.")
    print()

    translations = {
        "merhaba": "hello", "köpek": "dog", "kedi": "cat", "ev": "house", "masa": "table",
        "kalem": "pen", "kitap": "book", "araba": "car", "yemek": "food", "su": "water",
        "aşk": "love", "dost": "friend", "okul": "school", "elma": "apple", "kapı": "door",
        "pencere": "window", "ayakkabı": "shoe", "uçak": "plane", "tren": "train", "şehir": "city",
        "güneş": "sun", "ay": "moon", "yıldız": "star", "kış": "winter", "yaz": "summer",
        "ilkbahar": "spring", "sonbahar": "autumn", "deniz": "sea", "nehir": "river", "göl": "lake",
        "dağ": "mountain", "orman": "forest", "hayvan": "animal", "kuş": "bird", "balık": "fish",
        "insan": "person", "adam": "man", "kadın": "woman", "çocuk": "child", "bebek": "baby",
        "ağaç": "tree", "çiçek": "flower", "bahçe": "garden", "göz": "eye", "kulak": "ear",
        "burun": "nose", "ağız": "mouth", "el": "hand", "ayak": "foot", "bacak": "leg",
        "kol": "arm", "baş": "head", "saç": "hair", "gömlek": "shirt", "pantolon": "trousers",
        "ceket": "jacket", "çorap": "socks", "şapka": "hat", "dondurma": "ice cream", "pasta": "cake",
        "çay": "tea", "kahve": "coffee", "süt": "milk", "şeker": "sugar", "tuz": "salt",
        "karabiber": "pepper", "zeytin": "olive", "peynir": "cheese", "yumurta": "egg", "bal": "honey",
        "ekmek": "bread", "domates": "tomato", "salatalık": "cucumber", "soğan": "onion", "patates": "potato",
        "havuç": "carrot", "muz": "banana", "portakal": "orange", "üzüm": "grape", "çilek": "strawberry",
        "karpuz": "watermelon", "kavun": "melon", "yağmur": "rain", "kar": "snow", "rüzgar": "wind",
        "hava": "weather", "sıcak": "hot", "soğuk": "cold", "güzel": "beautiful", "çirkin": "ugly",
        "büyük": "big", "küçük": "small", "uzun": "long", "kısa": "short", "hızlı": "fast",
        "yavaş": "slow", "zor": "difficult", "kolay": "easy", "mutlu": "happy", "üzgün": "sad",
        "sinirli": "angry", "korkmuş": "scared", "yorgun": "tired", "hasta": "sick", "iyi": "good",
        "kötü": "bad", "temiz": "clean", "kirli": "dirty", "aç": "hungry", "susamış": "thirsty",
        "gün": "day", "gece": "night", "sabah": "morning", "öğle": "noon", "akşam": "evening",
        "yarın": "tomorrow", "bugün": "today", "dün": "yesterday", "hafta": "week", "ay": "month",
        "yıl": "year", "saat": "hour", "dakika": "minute", "saniye": "second", "zaman": "time",
        "para": "money", "iş": "job", "meslek": "profession", "doktor": "doctor", "öğretmen": "teacher",
        "öğrenci": "student", "polis": "police", "mühendis": "engineer", "hemşire": "nurse", "şoför": "driver",
        "sanatçı": "artist", "müzik": "music", "şarkı": "song", "film": "movie", "kitaplık": "bookshelf",
        "bilgisayar": "computer", "telefon": "phone", "televizyon": "television", "radyo": "radio", "internet": "internet",
        "oyun": "game", "spor": "sport", "futbol": "football", "basketbol": "basketball", "voleybol": "volleyball",
        "yüzme": "swimming", "koşu": "running", "dans": "dance", "resim": "painting", "fotoğraf": "photograph",
        "renk": "color", "kırmızı": "red", "mavi": "blue", "yeşil": "green", "sarı": "yellow",
        "siyah": "black", "beyaz": "white", "mor": "purple", "turuncu": "orange", "pembe": "pink",
        "gri": "gray", "kahverengi": "brown"
    }

    # Ask how many rounds the user wants
    total_words = len(translations)
    print(f"We have {total_words} Turkish words to quiz you on! 🇹🇷")
    while True:
        try:
            rounds = int(input("How many words do you want to be quizzed on? "))
            if 1 <= rounds <= total_words:
                break
            else:
                print(f"Please enter a number between 1 and {total_words} 🧠")
        except:
            print("Please enter a valid number! 🔢")

    words = list(translations.items())
    random.shuffle(words)

    score = 0
    for i in range(rounds):
        turkish, english = words[i]
        print()
        answer = input(f"What is the English translation for '{turkish}'? ").strip().lower()
        if answer == english:
            print("✅ That is correct! 🎉")
            score += 1
        else:
            print(f"❌ That is incorrect. The correct translation is '{english}'. 🤓")

    print("\n📊 You got", score, "/", rounds, "correct!")
    if score == rounds:
        print("🏆 Perfect score! You're a Turkish master! 🇹🇷✨")
    elif score > rounds // 2:
        print("👍 Great job! Keep practicing and you'll master them all!")
    else:
        print("📚 Don’t worry! Every mistake is a step to learning. Try again soon! 💪")

if __name__ == "__main__":
    main()
