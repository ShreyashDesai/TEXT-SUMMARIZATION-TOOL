# 🧠 TEXT-SUMMARIZE-TOOL

**Company:** CodTech IT Solutions  
**Name:** Shreyash Nhanu Desai  
**Intern ID:** CT04DR1291  
**Domain:** Artificial Intelligence  
**Duration:** 4 Weeks  
**Mentor:** Neela Santosh  

---

## 📘 Project Overview

The **Text Summarize Tool** is an AI-based project that uses **Natural Language Processing (NLP)** to automatically generate concise summaries from lengthy articles or text documents.  

This tool showcases how transformer models can understand language context and extract meaningful insights — helping users save time and enhance productivity.  

---

## 🚀 Features

- 🧩 Summarizes long paragraphs into clear, short text  
- ⚙️ Uses cutting-edge **transformer models** for accuracy  
- 💬 Simple **command-line interface (CLI)** for easy use  
- 🌍 Supports **multiple languages** (via Hugging Face multilingual models)  
- 💾 Lightweight and portable  

---

## 🛠️ Technologies Used

| Category | Technology |
|-----------|-------------|
| **Language** | Python |
| **Libraries** | `transformers`, `torch`, `nltk` |
| **Model** | `sshleifer/distilbart-cnn-12-6` |

---

## 💻 How to Run

### 🪜 Step 1 — Install Git (64-bit)

If Git isn’t installed, download the **64-bit** version from:  
👉 https://git-scm.com/downloads

During setup, **check** ✅ “Add Git to PATH”.

To verify installation:  
```bash
git --version
```

---

### 🪜 Step 2 — Install or Repair Python

Download and install Python (64-bit):  
👉 https://www.python.org/downloads/

✅ **Important:** During setup, check the box:  
```
Add Python to PATH
```

---

### 🧰 If Python Isn’t Working Even After Installing

If `python --version` shows *“not recognized”*, follow these fixes 👇  

#### 🪜 A. Verify Python Path  
Check your installation folder:  
```
C:\Users\<YourUsername>\AppData\Local\Programs\Python\
```

Inside, open the `Scripts` folder. Example:  
```
C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python312\Scripts
```

---

#### 🪜 B. Add Python to PATH (Manually)

1. Press **Win + R**, type `sysdm.cpl`, and press Enter.  
2. Go to **Advanced → Environment Variables**  
3. Under **System variables**, select `Path` → click **Edit**  
4. Click **New** and paste both:  
   ```
   C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python312\
   C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python312\Scripts\
   ```
5. Click **OK** on all dialogs.  

---

#### 🪜 C. Verify Setup  
Open a new CMD or PowerShell window and run:  
```bash
python --version
pip --version
```
If both return versions (e.g., `Python 3.12.2` and `pip 25.x`), you're good ✅  

#### 🪜 D. Upgrade pip (optional)  
```bash
python -m pip install --upgrade pip
```

💡 **Pro Tip:** If problems continue, install Python from the **Microsoft Store** (it sets PATH automatically).

---

### 🪜 Step 3 — Clone the Repository

```bash
git clone https://github.com/ShreyashDesai/TEXT-SUMMARIZATION-TOOL.git
cd TEXT-SUMMARIZATION-TOOL
```

---

### 🪜 Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🪜 Step 5 — Run the Program

```bash
python text_summarize_tool.py
```

Enter any paragraph or article — the tool will automatically generate a summarized version.

---

## 🧩 Example Output

**Input:**  
> Artificial Intelligence (AI) is transforming industries by automating complex tasks, improving decision-making, and driving innovation...

**Summary:**  
> AI enhances automation, innovation, and decision-making across industries.

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/cbf5cc21-682d-49d5-945b-f70e17b89c73" width="80%" alt="App Screenshot"/>
</p>

---

## 🧠 Model Information

**Model Used:** `sshleifer/distilbart-cnn-12-6`  
A distilled version of BART optimized for fast and high-quality text summarization.

---

## 👨‍💻 Author

**Shreyash Nhanu Desai**  
*Intern at CodTech IT Solutions*  

📧 **Email:** sheyashsn.desai@gmail.com  
🔗 **GitHub:** https://github.com/ShreyashDesai  
🔗 **LinkedIn:** https://www.linkedin.com/in/shreyash-desai-a13730384/  

---

## 🏁 Acknowledgements

I sincerely thank **CodTech IT Solutions** and my mentor **Neela Santosh** for their valuable guidance and support throughout this internship.  

---

✅ **Ready to use!**  
Clone, install, and summarize any text instantly.  
