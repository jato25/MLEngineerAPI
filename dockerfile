FROM conda/c3i-linux-64
COPY . .

RUN conda create --name env --file requeriments.txt -c conda-forge
SHELL ["conda", "run", "-n", "env", "/bin/bash", "-c"]

WORKDIR /api
EXPOSE 8080
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "env", "python", "run.py"]