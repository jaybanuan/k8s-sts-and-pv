# syntax=docker/dockerfile:1.4
FROM nginx/unit:1.28.0-python3.10

ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"

# Install poetry
RUN curl -sSL https://install.python-poetry.org/ | python3 -

# Install app
COPY k8s_sts_and_pv_backend/ /www/k8s_sts_and_pv_backend/
COPY poetry.lock pyproject.toml README.md /www/
RUN <<EOF
  cd /www/
  poetry config virtualenvs.create false
  poetry install --without dev --no-interaction --no-ansi
EOF

# Copy NGINX Unit config file
COPY config.json /docker-entrypoint.d/config.json

# create mount point
RUN <<EOF
  mkdir /data
  chown unit:unit /data
EOF