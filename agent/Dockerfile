FROM python:3.11-slim

# For building & running web tasks the agent may trigger (optional but handy)
RUN apt-get update && \
    apt-get install -y --no-install-recommends git curl ca-certificates nodejs npm && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip

# Create a non-root user
ARG USER=runner
ARG UID=1000
RUN useradd -m -u ${UID} ${USER}

COPY requirements.txt /tmp/requirements.txt
# Python deps (install from requirements.txt with setuptools fix for distutils)
RUN pip install --upgrade pip setuptools && \
    pip install -r /tmp/requirements.txt --no-cache-dir && \
    rm /tmp/requirements.txt
# Workdir where we mount the host repo
WORKDIR /workspace

# Copy a tiny entrypoint
COPY agent/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh && chown ${USER}:${USER} /workspace

USER ${USER}

# Default env for CrewAI using OpenAI-compatible endpoints
ENV OPENAI_API_KEY=sk-local-anything \
    OPENAI_API_BASE=http://litellm:4000/v1 \
    PYTHONUNBUFFERED=1

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
