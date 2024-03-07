SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Import SF1
cd /root/datasets/sf10/snapshot
lgraph_import -c ${SCRIPT_DIR}/import.conf --overwrite 1 \
    --dir /root/lgraph_db_sf10 --delimiter "|" --v3 0
cd $SCRIPT_DIR