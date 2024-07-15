# Food Recipe Generator

![Food Recipe Generator](https://your-image-url.com/banner.png) <!-- Replace with your banner image URL -->

## Overview

The Food Recipe Generator is a web application that allows users to upload an image of any food item and receive the ingredients and detailed instructions on how to make it. If the uploaded image is not recognized as food, the application returns an error message.

## Features

- Upload images in JPG, JPEG, or PNG format.
- Detects if the uploaded image is a food item.
- Generates a detailed recipe, including ingredients and step-by-step instructions.
- User-friendly interface for uploading images and displaying results.

## Technologies Used

- **Flask**: Web framework for building the application.
- **Google Generative AI (Gemma)**: For generating the recipe from the food image.
- **PIL (Python Imaging Library)**: For handling image operations.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Google Generative AI API key

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/alcatere/food_recipes_llm.git
   cd food_recipes_llm