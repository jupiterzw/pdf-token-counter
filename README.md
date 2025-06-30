# PDF Token Counter

A Python tool for analyzing PDF documents and counting tokens using OpenAI's tiktoken library. Perfect for estimating token usage before sending documents to AI models like GPT-4.

## 🚀 Features

- **Single File Analysis**: Analyze individual PDF files for token and character counts
- **Batch Processing**: Process entire folders of PDFs with comprehensive statistics
- **Markdown Reports**: Generate beautiful, formatted reports in Markdown
- **Multiple Token Models**: Support for different GPT models (GPT-4, GPT-3.5, etc.)
- **Automatic File Management**: Reports are automatically saved to `sample_analysis/` folder
- **Comprehensive Statistics**: Includes totals, averages, min/max values, and ranges

## 📋 Requirements

- Python 3.7+
- PyMuPDF (fitz)
- tiktoken

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd pdf-token-counter
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install PyMuPDF tiktoken
   ```

## 📖 Usage

### Single PDF File Analysis

```bash
python count_pdf_tokens.py path/to/your/file.pdf
```

**Output:**
- Token count and character count
- Report saved to `sample_analysis/filename_analysis_TIMESTAMP.md`

### Folder Analysis

```bash
python count_pdf_tokens.py path/to/your/folder/
```

**Output:**
- Individual file statistics in a table format
- Summary statistics (totals, averages)
- Additional insights (min/max values, ranges)
- Report saved to `sample_analysis/foldername_analysis_TIMESTAMP.md`

## 📊 Example Output

### Single File Report
```markdown
# Single PDF Analysis Report
**File:** `chapter_1.pdf`

## Statistics

| Metric | Value |
|--------|-------|
| **Tokens** | 1,990 |
| **Characters** | 7,799 |

**Estimated number of tokens:** 1,990
**Text length:** 7,799 characters
```

### Folder Report
```markdown
# PDF Token Analysis Report
**Folder:** `sample_pdf\sc4`
**Files Found:** 23 PDF file(s)

## Individual File Analysis

| File Name | Tokens | Characters |
|-----------|--------|------------|
| chapter_1.pdf | 1,990 | 7,799 |
| chapter_2.pdf | 3,119 | 10,186 |
| ... | ... | ... |

## Summary Statistics

| Metric | Value |
|--------|-------|
| **Files Processed** | 23 |
| **Total Tokens** | 61,622 |
| **Total Characters** | 192,266 |
| **Average Tokens per File** | 2,679 |
| **Average Characters per File** | 8,359 |

## Additional Insights

- **Largest file by tokens:** 5,518 tokens
- **Smallest file by tokens:** 1,326 tokens
- **Token range:** 4,192 tokens
- **Character range:** 10,537 characters
```

## 🔧 How It Works

### Core Logic

1. **PDF Text Extraction**: Uses PyMuPDF (fitz) to extract text from PDF files
2. **Token Counting**: Uses OpenAI's tiktoken library to count tokens according to GPT model specifications
3. **File Processing**: Automatically detects whether input is a file or folder
4. **Report Generation**: Creates formatted Markdown reports with comprehensive statistics

### Key Functions

- `extract_text_from_pdf()`: Extracts text from PDF using PyMuPDF
- `count_tokens()`: Counts tokens using tiktoken for specified model
- `process_single_pdf()`: Processes individual PDF files
- `process_folder()`: Processes entire folders with batch statistics
- `save_to_file()`: Saves reports to `sample_analysis/` folder

### Token Counting Logic

The tool uses OpenAI's tiktoken library which:
- Implements the same tokenization as GPT models
- Provides accurate token counts for cost estimation
- Supports different models (GPT-4, GPT-3.5, etc.)
- Handles various text encodings and special characters

## 📁 Project Structure

```
pdf-token-counter/
├── count_pdf_tokens.py      # Main script
├── sample_pdf/              # Sample PDF files for testing
│   └── sc4/                 # Example folder with PDFs
├── sample_analysis/         # Generated reports (auto-created)
│   ├── sc4_analysis_*.md    # Folder analysis reports
│   └── chapter_*_analysis_*.md  # Single file reports
└── README.md               # This file
```

## 🎯 Use Cases

- **Content Planning**: Estimate token usage before sending documents to AI models
- **Cost Estimation**: Calculate potential costs for AI processing
- **Document Analysis**: Understand the size and complexity of document collections
- **Batch Processing**: Analyze large collections of PDFs efficiently
- **Reporting**: Generate professional reports for documentation

## 🔍 Technical Details

### Dependencies

- **PyMuPDF**: High-performance PDF processing library
- **tiktoken**: OpenAI's tokenizer for accurate token counting
- **Built-in modules**: `os`, `sys`, `glob`, `datetime` (no installation required)

### Error Handling

- File existence validation
- PDF format validation
- Graceful error messages
- Exception handling for corrupted files

### Performance

- Efficient text extraction from PDFs
- Memory-conscious processing for large files
- Sorted file processing for consistent results


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
