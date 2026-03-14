import pyttsx3

# initialize voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_response(text):

    text = text.lower().strip()

    # greetings
    if any(word in text for word in ["hello", "hi", "hey", "good morning", "good evening"]):
        response = "Hello! I am your AI fitness trainer. You can ask me about workouts, diet, muscles, or say start workout to begin pushup tracking."

    # pushups
    elif any(word in text for word in ["pushup", "push-up", "push ups"]):
        response = "Pushups strengthen your chest, shoulders, triceps, and core. Beginners can start with 10 to 15 pushups and gradually increase."

    # workout
    elif any(word in text for word in ["workout", "exercise routine", "training"]):
        response = "A good workout includes strength training, cardio, and stretching. Try to stay consistent at least 4 to 5 days a week."

    # muscles
    elif any(word in text for word in ["muscle", "muscle gain", "build muscle"]):
        response = "Muscle growth happens with regular training, proper protein intake, and enough rest for recovery."

    # beginner fitness
    elif any(word in text for word in ["beginner", "start fitness", "new workout"]):
        response = "If you are a beginner, start with pushups, squats, planks, and light cardio for about 20 to 30 minutes."

    # abs
    elif any(word in text for word in ["abs", "six pack", "six-pack", "core workout"]):
        response = "To build abs, focus on planks, crunches, leg raises, and maintain a clean balanced diet."

    # weight loss
    elif any(word in text for word in ["lose weight", "weight loss", "fat loss"]):
        response = "Weight loss happens when you burn more calories than you consume. Combine cardio, strength training, and healthy eating."

    # cardio
    elif any(word in text for word in ["cardio", "running", "cycling", "jogging"]):
        response = "Cardio exercises like running, cycling, skipping, or brisk walking improve heart health and burn calories."

    # diet
    elif any(word in text for word in ["diet", "nutrition", "healthy food"]):
        response = "A balanced diet should include protein, carbohydrates, healthy fats, vegetables, fruits, and enough water."

    # protein
    elif any(word in text for word in ["protein", "protein food", "high protein"]):
        response = "Protein helps repair and build muscles. Good sources include eggs, chicken, fish, milk, lentils, beans, and nuts."

    # water
    elif any(word in text for word in ["water", "hydration", "drink water"]):
        response = "Staying hydrated is important for workout performance and recovery. Drink water before, during, and after exercise."

    # warmup
    elif any(word in text for word in ["warm up", "warmup", "prepare for workout"]):
        response = "Always warm up before exercising. It increases blood flow and reduces the risk of injury."

    # rest
    elif any(word in text for word in ["rest", "recovery", "rest day"]):
        response = "Rest days are important because muscles grow and repair during recovery."

    # motivation
    elif any(word in text for word in ["motivate", "motivation", "inspire"]):
        response = "Stay consistent and trust the process. Every small workout brings you closer to your fitness goal."

    # plank
    elif any(word in text for word in ["plank", "core plank"]):
        response = "Planks strengthen your core, shoulders, and back. Beginners can start with 20 seconds and increase gradually."

    # squat
    elif any(word in text for word in ["squat", "squats", "leg exercise"]):
        response = "Squats strengthen your legs, glutes, and core. Start with bodyweight squats before adding weights."

    # calories
    elif any(word in text for word in ["calorie", "calories", "energy intake"]):
        response = "Calories provide energy for your body. Managing calorie intake helps with weight loss or muscle gain."

    # sleep
    elif any(word in text for word in ["sleep", "rest at night", "good sleep"]):
        response = "Sleep is essential for muscle recovery and overall health. Aim for 7 to 8 hours every night."

    # stretching
    elif any(word in text for word in ["stretch", "stretching", "flexibility"]):
        response = "Stretching improves flexibility, reduces muscle tension, and helps prevent injuries."

    # gym
    elif any(word in text for word in ["gym", "fitness center"]):
        response = "Going to the gym can help with structured workouts, but home workouts can also keep you fit."

    # progress
    elif any(word in text for word in ["progress", "fitness progress", "workout improvement"]):
        response = "Tracking your workouts helps measure improvement. Small daily progress leads to big long-term results."

    else:
        response = "I can help with fitness questions or start your workout. Try asking about pushups, diet, muscles, cardio, or motivation."

    # speak response
    speak(response)

    return response