import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

class AnomalyDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Anomaly Detection System")
        self.root.geometry("500x300")
        
        self.label = tk.Label(root, text="Upload a CSV file for anomaly detection", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.upload_button = tk.Button(root, text="Upload File", command=self.upload_file)
        self.upload_button.pack(pady=10)
        
        self.detect_button = tk.Button(root, text="Detect Anomalies", command=self.detect_anomalies, state=tk.DISABLED)
        self.detect_button.pack(pady=10)
        
        self.file_path = ""
        self.df = None
    
    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.file_path = file_path
            self.df = pd.read_csv(file_path)
            messagebox.showinfo("Success", "File uploaded successfully!")
            self.detect_button.config(state=tk.NORMAL)
    
    def detect_anomalies(self):
        if self.df is None:
            messagebox.showerror("Error", "No file uploaded.")
            return
        
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        if numeric_cols.empty:
            messagebox.showerror("Error", "No numerical data found in the file.")
            return
        
        data = self.df[numeric_cols].fillna(self.df[numeric_cols].mean())
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)
        
        model = IsolationForest(contamination=0.05, random_state=42)
        self.df['Anomaly'] = model.fit_predict(data_scaled)
        
        plt.figure(figsize=(10, 6))
        plt.scatter(self.df.index, data_scaled[:, 0], c=self.df['Anomaly'], cmap='coolwarm')
        plt.xlabel("Index")
        plt.ylabel("First Numeric Feature (Scaled)")
        plt.title("Anomaly Detection Result")
        plt.show()
        
        messagebox.showinfo("Detection Complete", "Anomaly detection completed! Check the graph.")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = AnomalyDetectionApp(root)
    root.mainloop()
