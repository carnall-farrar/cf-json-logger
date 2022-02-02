from datetime import datetime
import pathlib
from pythonjsonlogger import jsonlogger


class CarnallFarrarJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CarnallFarrarJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get("asctime"):
            now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            log_record["asctime"] = now
        if not log_record.get("pathname"):
            pathname = pathlib.Path(__file__).parent.resolve()
            log_record["pathname"] = pathname
        if not log_record["processName"]:
            process_name = "Unknown Process"
            log_record["processName"] = process_name
