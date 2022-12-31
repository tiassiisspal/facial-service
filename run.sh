#!/bin/bash
echo "Iniciando o processo de RUN--------------->"

echo "================> Run do (portainer/portainer) local ...!!!"
### iniciar o para containar da api recon-facial
sudo docker run -d -p 5002:5002 tiassiisspal/recon-facial

echo "================> Run do portainer/portainer local ...!!!"
### iniciar o para conteiner do portainer/portainer local
sudo docker run -d -p 9000:9000 --name portainer --restart always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /home/carlosroberto/Projetos/Portainer/data:/data portainer/portainer

echo "----------------> Processo Finalizado com Sucesso!!!"