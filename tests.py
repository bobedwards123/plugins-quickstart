print('running tests for the project')

# Path: main.py
from utils import create_presentation_new


new_schema = {
  "slide_data": [
      {
      "heading": "Introduction to Dogs",
      "content": [
          "Dogs, also known as Canis lupus familiaris, are domesticated mammals that are commonly kept as pets",
          "They are known for their loyalty and companionship."
      ]
      },
           {
      "heading": "Introduction to Dogs",
      "content": [
          "Dogs, also known as Canis lupus familiaris, are domesticated mammals that are commonly kept as pets",
          "They are known for their loyalty and companionship."
      ]
      }
  ]
}

slide_data =new_schema['slide_data']
presentation_file = create_presentation_new(slide_data, "./presentations")
print(presentation_file)

    