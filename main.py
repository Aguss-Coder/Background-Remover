import os
from datetime import datetime
from rembg import remove

class BackgroundRemover:
  def __init__(self, input_folder, output_folder):
    self.input_folder = input_folder
    self.output_folder = output_folder

  def process_image(self):
    today = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    proccessed_folder = os.path.join(self.output_folder, today)
    os.makedirs(proccessed_folder, exist_ok=True)

    for filename in os.listdir(self.input_folder):
      if filename.endswith(('.png','.jpg', '.jpeg')):
        input_path = os.path.join(self.input_folder, filename)
        output_path = os.path.join(proccessed_folder, filename)
        self._remove_background(input_path, output_path)
        self._move_originals(input_path, proccessed_folder)

  def _remove_background(self, input_path, output_path):
    with open(input_path, 'rb') as inp, open(output_path, 'wb') as outp:
      background_output = remove(inp.read())
      outp.write(background_output)

  def _move_originals(self, input_path, destination_path):
    originals_folder = os.path.join(destination_path, 'originals')
    os.makedirs(originals_folder, exist_ok=True)

    filename = os.path.basename(input_path)
    new_path = os.path.join(originals_folder, filename)
    os.rename(input_path, new_path)
    
if __name__ == '__main__':
  input_folder = "input"
  output_folder = "output"

  remover = BackgroundRemover(input_folder, output_folder)
  remover.process_image()