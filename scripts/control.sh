SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


# Import SF1
function import_sf1() {
    cd /root/datasets/sf1/snapshot
    lgraph_import -c ${SCRIPT_DIR}/import.conf --overwrite 1 \
        --dir /root/lgraph_db_sf1 --delimiter "|" --v3 0
    cd -
}

function start_sf1() {
    lgraph_server --directory /root/lgraph_db_sf1 \
        --log_dir /root/lgraph_log_sf1 -d start
}

$1