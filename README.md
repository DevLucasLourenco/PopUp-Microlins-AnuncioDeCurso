# PopUp-Microlins-AnuncioDeCurso

<div align='center'>
  <h2>
    Este é um projeto que desenvolvi para a empresa Microlins. 
  </h2>
</div>

Nele, criei uma interface gráfica interativa onde o intuito da mesma é mostrar ao cliente uma janela contendo as datas dos eventos que terão.

Caso o cliente se interesse, basta clicar no botão de cadastrar-se que irá abrir uma janela onde poderá estar escaneando o QRCode.
Após isso, será levado à conversa designada, já com a resposta construída através da API `<wa.me>` do whatsapp. 

Caso o celular ou a pessoa tenha dificuldades em ler o QrCode, tem um botão chamado "Whatsapp Web".
Nele, a pessoa abrirá o Whatsapp no seu celular e irá conectar diretamente através da [Minha API, o AllWhatsPy - AWP](https://github.com/devlucaslourenco/allwhatspy).

Após a conexão ser realizada, todo o processo de conexão, recepção de dados pessoais (como o nome que o cliente inseriu no seu whatsapp, para aparecer automaticamente), envio de mensagem e desconexão serão feitos automaticamente.



Para esta aplicação, desenvolvi também um `.exe` e um `setup instalador`, para não precisar ficar passando os arquivos de máquina em máquina. 
Entretando, por serem arquivos pesados, não foi possível trazê-los a este repositório.
