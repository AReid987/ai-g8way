import uuid
import datetime
import logging
import os
from dotenv import load_dotenv
from langfuse import Langfuse

load_dotenv()


class LangfuseClient:
    def __init__(self):
        self.langfuse = Langfuse(
            public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
            secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
            url="https://cloud.langfuse.com",
        )

        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        logging.info("LangfuseClient initialized")

    def generate_session_id(self):
        timestamp = datetime.datetime.now().isoformat()
        uuid_str = str(uuid.uuid4())
        session_id = f"{timestamp}_{uuid_str}"
        logging.info(f"Generated session ID: {session_id}")

        return session_id

    def start_trace(self, trace_name: str, metadata: dict = None):
        trace = self.langfuse.trace(name=trace_name)

        if metadata:
            trace.metadata = metadata

        return trace

    def end_trace(self, trace, status_code: int, metadata: dict = None):
        end_time = datetime.datetime.now().timestamp()

        if metadata:
            trace.metadata.update(metadata)
        trace.end(end_time=end_time, status=str(status_code))
        logging.info(
            f"Trace '{trace.name}' ended with status {status_code} and metadata: {metadata}"
        )

    def get_langfuse_client(self):
        """Returns the initialized Langfuse client instance."""
        return self.langfuse
