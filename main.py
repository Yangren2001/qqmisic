# encoding=utf-8

"""
    @Project ：qqmusic 
    @File：main
    @Time:2024/2/29 20:44
    @Author:YR
    @describe:

"""
from Package.Spader import Spader

def main():
    spader = Spader()
    tag_df = spader.get_all_tag()  # 获取分类标签数据
    # print(tag_df)
    for id in tag_df["id"]:
        spader.get_class_song_list(id)
        # break


if __name__ == "__main__":
    main()

