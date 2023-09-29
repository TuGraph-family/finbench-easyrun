SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

lgraph_server -d stop
lgraph_server --directory /root/lgraph_db_sf10 \
    --log_dir /root/lgraph_log_sf10 -d start