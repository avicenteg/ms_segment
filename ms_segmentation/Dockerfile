FROM ubuntu:latest
WORKDIR /code
RUN apt-get -y update
RUN apt-get -y install git
RUN apt-get -y install python3.10
RUN apt-get -y install pip

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV nnUNet_raw_data_base="/code/model/nnUNet_raw_data"
ENV nnUNet_preprocessed="/code/model/nnUNet_preprocessed"
ENV RESULTS_FOLDER="/code/model/nnUNet_trained_models"

COPY requirements.txt requirements.txt
RUN pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
RUN pip install -r requirements.txt


EXPOSE 5000
COPY . .
CMD ["flask", "run"]
