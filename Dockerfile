# This should be sodadata/soda-library:xxx
# The version should be fixed and aligned with the version of this action.
ARG SODA_LIBRARY_VERSION=latest
FROM sodadata/soda-library:$SODA_LIBRARY_VERSION

RUN apt-get update && apt-get install -y lsof

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]