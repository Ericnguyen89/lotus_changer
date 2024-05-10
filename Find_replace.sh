#!/bin/bash

# Hàm tìm kiếm và thay thế giá trị từ file io3_mac.conf trong một thư mục và các thư mục con
# Tham số:
# $1: Thư mục chứa file io3_mac.conf
search_and_replace() {
    folder=$1

    # Kiểm tra xem thư mục tồn tại không
    if [ ! -d "$folder" ]; then
        echo "Thư mục $folder không tồn tại."
        return 1
    fi

    # Lặp qua tất cả các file và thư mục trong thư mục hiện tại
    for item in "$folder"/*; do
        if [ -d "$item" ]; then
            # Nếu là thư mục, gọi lại hàm đệ quy với thư mục con
            search_and_replace "$item"
        elif [ -f "$item" ]; then
            # Nếu là tệp, kiểm tra xem có phải là tệp io3_mac.conf không
            if [ "$(basename "$item")" = "io3_mac.conf" ]; then
                # Đọc từng dòng từ tệp io3_mac.conf
                while IFS='=' read -r key value; do
                    # Kiểm tra xem dòng đó có định dạng key=value không
                    if [[ ! -z "$key" && ! -z "$value" ]]; then
                        # Thực hiện tìm kiếm và thay thế trong tất cả các tệp văn bản trong thư mục
                        grep -rl "$key" "$folder" | xargs sed -i "s/$key/$value/g"
                    fi
                done < "$item"
            fi
        fi
    done
}

# Lấy đường dẫn thư mục chứa file io3_mac.conf
io3_mac_folder="$(dirname "$0")"

# Gọi hàm tìm kiếm và thay thế
search_and_replace "$io3_mac_folder"

echo "Quá trình tìm kiếm và thay thế đã hoàn thành."
