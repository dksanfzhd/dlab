import tkinter as tk
from tkinter import ttk
import pickle
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.title('BMI Calculator')

# Create a Notebook (tab view)
notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)

# Create tabs for different views
bmi_tab = ttk.Frame(notebook)
exercise_tab = ttk.Frame(notebook)
diet_tab = ttk.Frame(notebook)

notebook.add(bmi_tab, text="BMI Results")
notebook.add(exercise_tab, text="Exercise Recommendations")
notebook.add(diet_tab, text="Dietary Recommendations")

# Input fields and labels for BMI calculation
height_label = tk.Label(bmi_tab, text='Height (cm):')
height_label.pack()
height_entry = tk.Entry(bmi_tab)
height_entry.pack()

weight_label = tk.Label(bmi_tab, text='Weight (kg):')
weight_label.pack()
weight_entry = tk.Entry(bmi_tab)
weight_entry.pack()

# Result label for BMI
result_label = tk.Label(bmi_tab, text='')
result_label.pack()

# Add a label to display the doctor's image on the left
doctor_image = Image.open("doctor.png")  # Replace "doctor.png" with the path to your image
doctor_image = doctor_image.resize((90, 90), Image.LANCZOS)  # Adjust the size as needed
doctor_photo = ImageTk.PhotoImage(doctor_image)
doctor_label = tk.Label(bmi_tab, image=doctor_photo)
doctor_label.photo = doctor_photo  # To prevent the image from being garbage collected
doctor_label.pack(side="left")  # Set the side to "left" to place the image on the left


# Exercise and diet recommendations text widgets
exercise_text = tk.Text(exercise_tab, height=10, width=40, state="normal")
exercise_text.pack()

diet_text = tk.Text(diet_tab, height=10, width=40, state="normal")
diet_text.pack()

# Sample exercise recommendations based on BMI categories
exercise_recommendations = {
    0: "For individuals classified as Extremely Weak, it is essential to start with very light exercises such as gentle stretching and short walks. Consult with a healthcare professional before starting any exercise program.",
    1: "For those classified as Weak, low-impact exercises such as swimming, yoga, or light resistance training can help improve strength and stamina. Begin with short sessions and gradually increase intensity.",
    2: "If your BMI indicates Normal, maintain your health by staying physically active. Incorporate a mix of cardiovascular and strength training exercises into your routine.",
    3: "For individuals classified as Overweight, focus on aerobic exercises like walking, jogging, or cycling to burn calories and strength training to build muscle.",
    4: "Obesity requires a combination of regular exercise and dietary changes. Engage in both aerobic and strength training exercises for balanced fitness.",
    5: "Extreme Obesity demands a comprehensive approach. Consult with a healthcare provider to develop a tailored exercise plan that suits your capabilities and needs."
}

# Sample diet recommendations based on BMI categories
diet_recommendations = {
    0: "For individuals classified as Extremely Weak, prioritize nutrient-dense foods. Ensure you receive proper protein, vitamins, and minerals. Consider a liquid diet if needed.",
    1: "For those classified as Weak, focus on balanced meals with lean proteins, fruits, and vegetables. Adequate hydration is crucial.",
    2: "If your BMI indicates Normal, maintain a well-balanced diet with a variety of foods. Ensure a mix of carbohydrates, proteins, and healthy fats.",
    3: "For individuals classified as Overweight, monitor portion sizes and reduce sugar and high-calorie foods. Increase fiber intake through fruits and vegetables.",
    4: "Obesity requires calorie reduction and portion control. Emphasize a diet rich in fruits, vegetables, lean proteins, and whole grains. Avoid sugary and high-fat foods.",
    5: "Extreme Obesity demands a controlled diet under professional guidance. Consult a healthcare provider for a personalized plan that includes reduced calorie intake."
}

# Function to get exercise recommendations
def get_exercise_recommendations(bmi_category):
    return exercise_recommendations.get(bmi_category, "No exercise recommendations available.")

# Function to get diet recommendations
def get_diet_recommendations(bmi_category):
    return diet_recommendations.get(bmi_category, "No diet recommendations available.")

# Function to calculate BMI and update the results
def calculate_bmi():
    height = float(height_entry.get())
    weight = float(weight_entry.get())

    # BMI 모델을 불러오기
    with open(r'C:\Users\hjhan\OneDrive\첨부 파일\바탕 화면\model.pkl', 'rb') as model_file:
        loaded_model = pickle.load(model_file)

    # 모델을 사용하여 BMI를 예측
    predicted_bmi = int(loaded_model.predict([[height, weight]]))

    # Update the result label
    bmi_categories = ["Extremely Weak", "Weak", "Normal", "Overweight", "Obesity", "Extreme Obesity"]
    result_text = "BMI: {} ({})".format(predicted_bmi, bmi_categories[predicted_bmi])
    result_label.config(text=result_text)

    # Update exercise recommendations based on BMI
    exercise_text.config(state="normal")  # Allow editing
    exercise_text.delete(1.0, tk.END)  # Clear the text widget
    exercise_info = get_exercise_recommendations(predicted_bmi)
    exercise_text.insert(tk.END, exercise_info)
    exercise_text.config(state="disabled")  # Make it non-editable

    # Update dietary recommendations based on BMI
    diet_text.config(state="normal")  # Allow editing
    diet_text.delete(1.0, tk.END)  # Clear the text widget
    diet_info = get_diet_recommendations(predicted_bmi)
    diet_text.insert(tk.END, diet_info)
    diet_text.config(state="disabled")  # Make it non-editable

# Create the Calculate BMI button
calculate_button = tk.Button(bmi_tab, text='Calculate BMI', command=calculate_bmi)
calculate_button.pack()

# Run the tkinter main loop
window.mainloop()
