FROM python:3.10.2-alpine3.15

ARG USER=plana
ENV HOME /home/$USER

# install sudo as root
RUN apk add --update sudo

# add new user
RUN adduser -D $USER \
        && echo "$USER ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER \
        && chmod 0440 /etc/sudoers.d/$USER

USER $USER
WORKDIR $HOME

COPY ./requirements.txt $HOME/requirements.txt
RUN sudo chown -R $USER:$USER $HOME
RUN pip install -r requirements.txt

COPY ./app/ $HOME
RUN sudo chown -R $USER:$USER $HOME

ENTRYPOINT [ "python" ]
CMD [ "main.py" ]