import jinja2
from dataclasses import dataclass
from typing import List
import os
import shutil

title = 'Liu Liu - CUHK'
name = 'Liu Liu'

author_links = {
    "Liu Liu": "https://liuliu3dv.github.io",

}


@dataclass
class Author:
    name: str
    url: str


@dataclass
class Paper:
    tag: str
    title: str
    short_title: str
    conference: str
    conference_short: str
    year: int
    authors: List[Author]
    url: str
    url_arxiv: str
    url_project_page: str = None
    url_paper: str = None
    url_supp: str = None
    url_video: str = None
    url_poster: str = None
    url_code: str = None
    description: str = None
    image: str = None
    image_after: str = None
    video_after: str = None
    special_honor: str = None
    yellow_highlight: bool = False
    abstract: str = None
    affiliation: str = None
    bib: str = None

@dataclass
class Experience:
    title: str
    description: str



def gen_author_list(*author_names):
    authors = []
    for author_name in author_names:
        url = None
        for name, link in author_links.items():
            if author_name.startswith(name):
                break
        authors.append(Author(
            name=author_name,
            url=url
        ))
    return authors


def get_papers():
    papers = []
    papers.append(Paper(
        tag="xx",
        title="xx",
        short_title="xx",
        conference="xx",
        conference_short="xx",
        year=2025,
        authors=gen_author_list("Liu Liu*"),
        url="xx",
        url_paper="xx",
        url_arxiv="xx",
        # image="./images/xx.png",
        # special_honor="xx",
        # video_after="./images/xx.mp4"
    ))
    # papers.append(Paper(
    #     tag="arrangement",
    #     title="ArrangementNet: Learning Scene Arrangements for Vectorized Indoor Scene Modeling",
    #     short_title="ArrangementNet",
    #     conference="ACM Transactions on Graphics (TOG) ",
    #     conference_short="TOG'23",
    #     year=2023,
    #     authors=gen_author_list("Jingwei Huang", "Shanshan Zhang", "Bo Duan", "Liu Liu", "Minwei Sun", "Li Yi"),
    #     url="https://dl.acm.org/doi/10.1145/3592122",
    #     image="./images/arrangementnet.png",
    #     url_arxiv="",
    #     url_paper="https://dl.acm.org/doi/10.1145/3592122",
    #     special_honor="Journal Track"
    # ))
#     papers.append(Paper(
#         tag="liga",
#         title="LIGA-Stereo: Learning Lidar Geometry aware Representations for Stereo-based 3d Detector",
#         short_title="LIGA-Stereo",
#         conference="International Conference on Computer Vision (<b>ICCV</b>)",
#         conference_short="ICCV'21",
#         year=2021,
#         authors=gen_author_list("Liu Liu", "Shaoshuai Shi", "Xiaogang Wang", "Hongsheng Li"),
#         url="https://openaccess.thecvf.com/content/ICCV2021/html/Guo_LIGA-Stereo_Learning_LiDAR_Geometry_Aware_Representations_for_Stereo-Based_3D_Detector_ICCV_2021_paper.html",
#         url_arxiv="https://arxiv.org/abs/2108.08258",
#         url_paper="https://openaccess.thecvf.com/content/ICCV2021/html/Guo_LIGA-Stereo_Learning_LiDAR_Geometry_Aware_Representations_for_Stereo-Based_3D_Detector_ICCV_2021_paper.html",
#         # url_supp="https://openaccess.thecvf.com/content/ICCV2021/supplemental/Guo_LIGA-Stereo_Learning_LiDAR_ICCV_2021_supplemental.pdf",
#         url_poster=None,
#         url_code="https://github.com/xy-guo/LIGA-Stereo",
#         url_project_page="/liga",
#         image="./images/liga.png",
#         special_honor="Ranked 1st place among stereo-based 3D detection methods on KITTI (July 2021), refer to <a href=\"https://www.cvlibs.net/datasets/kitti/eval_object_detail.php?&result=d5d1938b704537150df7f8403d173aa16fe9ba17\">here</a>.",
#         abstract="Stereo-based 3D detection aims at detecting 3D object bounding boxes from stereo images using intermediate depth maps or implicit 3D geometry representations, which provides a low-cost solution for 3D perception. However, its performance is still inferior compared with LiDAR-based detection algorithms. To detect and localize accurate 3D bounding boxes, LiDAR-based models can encode accurate object boundaries and surface normal directions from LiDAR point clouds. However, the detection results of stereo-based detectors are easily affected by the erroneous depth features due to the limitation of stereo matching. To solve the problem, we propose LIGA-Stereo (LiDAR Geometry Aware Stereo Detector) to learn stereo-based 3D detectors under the guidance of high-level geometry-aware representations of LiDAR-based detection models. In addition, we found existing voxel-based stereo detectors failed to learn semantic features effectively from indirect 3D supervisions. We attach an auxiliary 2D detection head to provide direct 2D semantic supervisions. Experiment results show that the above two strategies improved the geometric and semantic representation capabilities. Compared with the state-of-the-art stereo detector, our method has improved the 3D detection performance of cars, pedestrians, cyclists by <strong>10.44%, 5.69%, 5.97%</strong> mAP respectively on the official KITTI benchmark. ",
#         affiliation="CUHK-SenseTime Joint Laboratory, The Chinese University of Hong Kong",
#         bib="""@InProceedings{Guo_2021_ICCV,
#     author = {Guo, Xiaoyang and Shi, Shaoshuai and Wang, Xiaogang and Li, Hongsheng},
#     title = {LIGA-Stereo: Learning LiDAR Geometry Aware Representations for Stereo-based 3D Detector},
#     booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
#     month = {October},
#     year = {2021}
# }
#         """
#     ))
#     papers.append(Paper(
#         tag="gwcnet",
#         title="Group-wise Correlation Stereo Network",
#         short_title="GwcNet",
#         conference="Conference on Computer Vision and Pattern Recognition (<b>CVPR</b>)",
#         conference_short="CVPR'19",
#         year=2019,
#         authors=gen_author_list("Liu Liu", "Kai Yang", "Wukui Yang", "Xiaogang Wang", "Hongsheng Li"),
#         url="https://openaccess.thecvf.com/content_CVPR_2019/html/Guo_Group-Wise_Correlation_Stereo_Network_CVPR_2019_paper.html",
#         url_arxiv="https://arxiv.org/abs/1903.04025",
#         url_paper="https://openaccess.thecvf.com/content_CVPR_2019/html/Guo_Group-Wise_Correlation_Stereo_Network_CVPR_2019_paper.html",
#         url_poster=None,
#         url_code="https://github.com/xy-guo/GwcNet",
#         image="./images/gwcnet.jpg",
#     ))
#     papers.append(Paper(
#         tag="unsupstereo",
#         title="Unsupervised Cross-Spectral Stereo Matching by Learning to Synthesize",
#         short_title=None,
#         conference="AAAI",
#         conference_short="AAAI'19",
#         year=2019,
#         authors=gen_author_list("Liu Liu*", "Mingyang Liang*", "Hongsheng Li", "Xiaogang Wang", "You Song"),
#         url="https://ojs.aaai.org/index.php/AAAI/article/view/4894",
#         url_arxiv="https://arxiv.org/abs/1903.01078",
#         url_paper="https://ojs.aaai.org/index.php/AAAI/article/view/4894",
#         image="./images/cs-stereo.jpg",
#         special_honor="Oral Presentation"
#     ))
#     papers.append(Paper(
#         tag="distillmono",
#         title="Learning Monocular Depth by Distilling Cross-domain Stereo Networks",
#         short_title=None,
#         conference="European Conference on Computer Vision (<b>ECCV</b>)",
#         conference_short="ECCV'18",
#         year=2018,
#         authors=gen_author_list("Liu Liu", "Hongsheng Li", "Shuai Yi", "Jimmy Ren", "Xiaogang Wang"),
#         url="https://openaccess.thecvf.com/content_ECCV_2018/html/Xiaoyang_Guo_Learning_Monocular_Depth_ECCV_2018_paper.html",
#         url_arxiv="https://arxiv.org/abs/1808.06586",
#         url_paper="https://openaccess.thecvf.com/content_ECCV_2018/html/Xiaoyang_Guo_Learning_Monocular_Depth_ECCV_2018_paper.html",
#         url_poster=None,
#         url_video="https://www.youtube.com/watch?v=QAcuYT7q_gY",
#         url_code="https://github.com/xy-guo/Learning-Monocular-Depth-by-Stereo",
#         image="./images/mono.jpg",
#     ))
#     papers.append(Paper(
#         tag="encap",
#         title="Neural Network Encapsulation",
#         short_title="Encap",
#         conference="European Conference on Computer Vision (<b>ECCV</b>)",
#         conference_short="ECCV'18",
#         year=2018,
#         authors=gen_author_list("Hongyang Li", "Liu Liu", "Bo Dai", "Wanli Ouyang", "Xiaogang Wang"),
#         url="https://openaccess.thecvf.com/content_ECCV_2018/html/Hongyang_Li_Neural_Network_Encapsulation_ECCV_2018_paper.html",
#         url_arxiv="https://arxiv.org/abs/1808.03749",
#         url_paper="https://openaccess.thecvf.com/content_ECCV_2018/html/Hongyang_Li_Neural_Network_Encapsulation_ECCV_2018_paper.html",
#         url_poster=None,
#         image="./images/encap.png",
#     ))

    return papers

def get_exp():
    exp = []
    exp.append(Experience(
        title="3D Vision Algorithm Engineer, March 2022 - Present, Horizon Robotics Inc.",
        description=""
    ))
    exp.append(Experience(
        title="3D Vision Algorithm Engineer, June 2019 - Oct 2021, Orbbec Inc",
        description="Working on 3D Depth Estimation, Stereo."
    ))
    return exp


def find_paper(startswith) -> Paper:
    papers = get_papers()
    for paper in papers:
        if paper.title.startswith(startswith):
            return paper
    return None


def render_index(filename="index.jinja"):
    render_data = dict(
        title=title,
        name=name,
        papers=get_papers(),
        # experience=get_exp()
    )
    subs = jinja2.Environment(
        loader=jinja2.FileSystemLoader('./')
    ).get_template(filename).render(**render_data)
    lines = subs.split("\n")
    lines = [line for line in lines if len(line.strip()) > 0]
    subs = '\n'.join(lines)

    with open(filename.replace(".jinja", ".html"), 'w') as f:
        f.write(subs)


# @dataclass
# class Project:
#     link: str
#     short_name: str
#     title: str
#     abstract: str
#     image: str
#     video: str
#     paper: Paper
#     pre_html: str = ""
#     extra_html: str = ""


# def render_project_pages(filename="project.jinja"):
#     projects = []

#     liga_paper = find_paper("LIGA")
#     projects.append(
#         Project(
#             link="liga",
#             short_name=liga_paper.short_title,
#             title=liga_paper.title,
#             abstract=liga_paper.abstract,
#             image=None,
#             video=liga_paper.url_video,
#             paper=liga_paper,
#             pre_html="""
#                 <center>
#                     <img src="/images/liga.png" alt="..." width="60%" />
#                 </center>
#             """,
#             extra_html="""
#                 <h4>Results<h4>
#                 <p>
#                     <center>
#                         <img src="/images/liga-demo.png" alt="..." width="100%" />
#                     </center>
#                 </p>        
#                 <h4>KITTI Benchmark<h4>
#                 <p>
#                     <center>
#                         <img src="/images/liga-kitti.png" alt="..." width="80%" />
#                     </center>
#                 </p>
#             """
#         )
#     )

#     for proj in projects:
#         render_data = dict(
#             project=proj,
#             paper=proj.paper,
#         )
#         subs = jinja2.Environment(
#             loader=jinja2.FileSystemLoader('./')
#         ).get_template(filename).render(**render_data)

#         dump_path = proj.link
#         if not os.path.isdir(dump_path):
#             os.mkdir(dump_path)
#         dump_file = os.path.join(dump_path, "index.html")
#         print("saving to", dump_file)
#         with open(dump_file, 'w') as f:
#             f.write(subs)


if __name__ == "__main__":
    render_index()
    # render_project_pages()