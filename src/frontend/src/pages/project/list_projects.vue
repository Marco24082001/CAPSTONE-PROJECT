<template>
    <div class="container">
        <div class="cp-projects">
            <div class="cp-project">
                <a
                    href="https://givenow.vn/du-an/chung-tay-cham-soc-suc-khoe-cho-200-tre-nhap-cu-tai-truong-tinh-thuong-ai-linh/"
                    class="image-index"
                >
                    <img src="@/assets/project_img/project-0.jpg" alt="" />
                </a>
                <div class="cp-content">
                    <h3>Chung tay hỗ trợ học</h3>
                    <!-- <span>$ 15.99</span> -->
                </div>
                <!-- <p>Lorem ipsum dolor sit amet consectetur adipisicing elit..</p> -->
            </div>

            <div class="cp-project">
                <a
                    href="https://givenow.vn/du-an/chung-tay-cham-soc-suc-khoe-cho-200-tre-nhap-cu-tai-truong-tinh-thuong-ai-linh/"
                    class="image-index"
                >
                    <img src="@/assets/project_img/project-3.jpg" alt="" />
                </a>
                <div class="cp-content">
                    <div class="cp-meta">
                        <a href="/#">Cộng đồng</a>
                    </div>
                    <h2 class="cp-title">
                        <a
                            href="https://givenow.vn/du-an/chung-tay-cham-soc-suc-khoe-cho-200-tre-nhap-cu-tai-truong-tinh-thuong-ai-linh/"
                            >Chung tay hỗ trợ học</a
                        >
                    </h2>
                    <div class="cp-progressbar"></div>
                    <!-- <span>$ 15.99</span> -->
                    <div class="cp-details">
                        <div class="cp-details-data">
                            <a class="cp-author-avatar" href="#">
                                <img
                                    src="https://givenow.vn/wp-content/uploads/2022/08/_resampled/File-Anh-Logo-Quy-Phan-Anh-fit-60-60.jpg"
                                />
                            </a>
                            <div class="cp-details-meta">
                                <div class="cp-author-meta">
                                    <a href="/#">Quỹ Xã hội Phan Anh</a>
                                </div>
                                <div class="cp-post-meta">
                                    <div class="cp-meta-date">Tháng 26, 2020</div>
                                </div>
                            </div>
                        </div>
                        <div class="cp-target"><span>100000 $</span></div>
                    </div>
                </div>
                <!-- <p>Lorem ipsum dolor sit amet consectetur adipisicing elit..</p> -->
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "List-Projects",
};
</script>

<style scoped lang="scss">
:root {
    --bodyBack: #ffeaed;
    --textColor: #1b2741;
    --starColor: #f67034;
    --sectionBack: #f7f6f9;
}

.container {
    width: 100vw;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    .cp-projects {
        width: 100%;
        align-self: center;
        // height: 65vh;
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 3rem;
        .cp-project {
            position: relative;
            background-color: var(--sectionBack);
            width: 20rem;
            // box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
            display: flex;
            flex-direction: column;
            transition: 0.3s;
            // &:hover {
            //     transform: translateY(-15px);
            //     box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
            // }
            .image-index {
                display: grid;
                overflow: hidden;
                place-content: center;
                img {
                    width: 100%;
                }
            }
            .cp-content {
                margin-top: 1.2rem;
                width: 100%;
                // display: flex;
                // justify-content: space-between;
                .cp-meta {
                    font-family: var(--cs-font-category-family), sans-serif;
                    font-size: var(--cs-font-category-size);
                    font-weight: var(--cs-font-category-weight);
                    font-style: var(--cs-font-category-style);
                    letter-spacing: var(--cs-font-category-letter-spacing);
                    text-transform: var(--cs-font-category-text-transform);
                    a {
                        color: var(--cs-color-category);
                        transition: 0.25s;
                        &:hover {
                            color: var(--cs-color-category-hover);
                        }
                    }
                }
                .cp-title {
                    font-family: var(--cs-font-headings-family), sans-serif;
                    font-weight: var(--cs-font-headings-weight);
                    text-transform: var(--cs-font-headings-text-transform);
                    line-height: var(--cs-font-headings-line-height);
                    letter-spacing: var(--cs-font-headings-letter-spacing);
                    font-size: 1.25rem;
                    margin-top: 0.5rem;
                    a {
                        display: block;
                        text-decoration: none;
                        color: var(--cs-color-title, var(--cs-color-primary));
                        transition: 0.25s;
                        &:hover {
                            color: var(--cs-color-title-hover, var(--cs-color-secondary));
                        }
                    }
                }
                .cp-details {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    flex-wrap: wrap;
                    width: 100%;
                    margin-top: 1rem;
                    .cp-details-data {
                        display: flex;
                        align-items: center;
                        flex-wrap: wrap;
                        .cp-author-avatar {
                            width: 40px;
                            border-radius: 50%;
                            // overflow: hidden;
                            img {
                                border-radius: 50%;
                                object-position: center;
                                object-fit: cover;
                                width: 40px;
                                height: 40px;
                            }
                        }
                        .cp-details-meta {
                            margin-left: 0.3rem;
                            display: flex;
                            flex-direction: column;
                            flex-wrap: wrap;
                            flex: 1;
                            font-family: var(--cs-font-post-meta-family), sans-serif;
                            font-size: var(--cs-font-post-meta-size);
                            font-weight: var(--cs-font-post-meta-weight);
                            font-style: var(--cs-font-post-meta-style);
                            letter-spacing: var(--cs-font-post-meta-letter-spacing);
                            text-transform: var(--cs-font-post-meta-text-transform);
                            .cp-post-meta {
                                // flex: 0 0 100%;
                                // width: 100%;
                            }
                        }
                    }

                    .cp-target {
                        span {
                            // display: inline-flex;
                            // align-items: center;
                            // justify-content: center;
                            // text-decoration: none;
                            // border: none;
                            // border-radius: var(--cs-primary-border-radius);
                            line-height: 1rem;
                            transition: 0.25s;
                            box-shadow: none;
                            cursor: pointer;
                            padding: 0.75rem 1.5rem;
                            border-radius: var(--cs-primary-border-radius);
                            --cs-color-style: var(--cs-color-button-contrast);
                            --cs-color-style-contrast: var(--cs-color-button);
                            --cs-color-style-border: var(--cs-color-contrast-200);
                            --cs-color-style-hover: var(--cs-color-button);
                            --cs-color-style-hover-contrast: var(--cs-color-button-contrast);
                            --cs-color-style-hover-border: var(--cs-color-button);
                            border: 1px solid var(--cs-color-style-border);
                            background-color: var(--cs-color-style);
                            color: var(--cs-color-style-contrast);
                            font-family: var(--cs-font-primary-family), sans-serif;
                            font-size: var(--cs-font-primary-size);
                            font-weight: var(--cs-font-primary-weight);
                            font-style: var(--cs-font-primary-style);
                            letter-spacing: var(--cs-font-primary-letter-spacing);
                            text-transform: var(--cs-font-primary-text-transform);
                        }
                    }
                }
            }
        }
    }
}

// .cp-content span {
//     font-size: 1.5em;
//     color: var(--starColor);
// }
// .cp-project p {
//     font-size: 18px;
//     line-height: 25px;
// }
// .stars svg {
//     font-size: 1.3em;
//     color: var(--starColor);
// }
// .bay {
//     position: absolute;
//     bottom: 20px;
//     right: 20px;
// }
// .bay button {
//     padding: 10px 20px;
//     border-radius: 7px;
//     border: none;
//     background-color: var(--textColor);
//     color: var(--sectionBack);
//     font-size: 18px;
//     text-transform: capitalize;
//     cursor: pointer;
//     transition: 0.5s;
// }
// .bay button:hover {
//     transform: scale(1.1);
// }
</style>
