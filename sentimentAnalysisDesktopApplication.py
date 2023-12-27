import tkinter as tk
from transformers import pipeline
from PIL import Image, ImageTk

class SentimentAnalysisApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sentiment Analysis on Social Media")
        self.master.geometry("500x300")
        self.master.configure(bg="#F0F0F0")  # Set background color

        self.label = tk.Label(master, text="Enter your message:", font=("Arial", 14), bg="#F0F0F0")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, width=40, font=("Arial", 12))
        self.entry.pack(pady=10)

        self.analyze_button = tk.Button(master, text="Analyze", command=self.analyze_sentiment, font=("Arial", 12), bg="#4CAF50", fg="white", relief=tk.GROOVE)
        self.analyze_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Arial", 16), bg="#F0F0F0")
        self.result_label.pack(pady=10)

        self.sentiment_analyzer = pipeline("sentiment-analysis")

        # Load images for sentiments
        self.positive_image = ImageTk.PhotoImage(Image.open("positive_image.png").resize((50, 50), resample=Image.Resampling.LANCZOS))
        self.negative_image = ImageTk.PhotoImage(Image.open("negative_image.png").resize((50, 50), resample=Image.Resampling.LANCZOS))

    def analyze_sentiment(self):
        message = self.entry.get()

        if message:
            result = self.sentiment_analyzer(message)[0]
            sentiment_label = result["label"]
            sentiment_score = result["score"]

            if sentiment_label == "POSITIVE":
                sentiment_image = self.positive_image
                text_color = "#008000"  # Green for positive
            elif sentiment_label == "NEGATIVE":
                sentiment_image = self.negative_image
                text_color = "#FF0000"  # Red for negative

            self.result_label.config(text=f"Score: {sentiment_score:.2f}", image=sentiment_image, compound=tk.LEFT, fg=text_color)
        else:
            self.result_label.config(text="Please enter a message.", image=None, fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = SentimentAnalysisApp(root)
    root.mainloop()
