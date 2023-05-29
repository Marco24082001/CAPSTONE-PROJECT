<template>
    <div class="cp-project">
        <!-- <router-link :to="{ name: 'Projectdetail', params: { id: 123 } }" class="image-index">
            <img :src="require('@/assets/project_img/' + project_img + '')" alt="" />
        </router-link> -->
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
            <div class="cp-progressbar">
                <div class="neo-progressbar">
                    <div></div>
                </div>
                <div class="fund-raised">
                    <div class="fund-raised-txt">40.000 đ</div>
                    <div class="fund-raised-percent">40%</div>
                </div>
            </div>
            <!-- <span>$ 15.99</span> -->
            <div class="cp-details">
                <div class="cp-details-data">
                    <div class="cp-details-meta">
                        <div class="cp-author-meta">
                            <a href="/#">Quỹ Xã hội Phan Anh</a>
                        </div>
                        <div class="cp-post-meta">
                            <div class="cp-meta-date">Tháng 26, 2020</div>
                        </div>
                    </div>
                </div>
                <div class="cp-fund-goal"><span>100.000 đ</span></div>
            </div>
        </div>
        <!-- <p>Lorem ipsum dolor sit amet consectetur adipisicing elit..</p> -->
    </div>
</template>

<script>
export default {
    name: "card-create",
};
</script>
<style scoped lang="scss">
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
        width: 100%;
        img {
            width: 100%;
            -webkit-transform: scale(1);
            transform: scale(1);
            -webkit-transition: 0.3s ease-in-out;
            transition: 0.3s ease-in-out;
        }
        &:hover img {
            -webkit-transform: scale(1.2);
            transform: scale(1.2);
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
        .cp-progressbar {
            padding: 0px;
            margin: 10px 0px 0px 0px;
            .neo-progressbar {
                border-radius: 6px;
                background-color: #ff2e5b1a;
                div {
                    height: 0.4rem;
                    border-radius: 6px;
                    width: 40px;
                    background-color: #ff2e5b;
                    z-index: 11111;
                }
            }
            .fund-raised {
                margin-top: 0.5rem;
                display: flex;
                justify-content: space-between;
            }
        }
        .cp-details {
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            width: 100%;
            margin-top: 0.5rem;
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
                    .cp-author-meta a {
                        font-weight: 500;
                        color: var(--cs-color-meta-links, var(--cs-color-primary));
                        &:hover {
                            color: var(--cs-color-meta-links-hover, var(--cs-color-secondary));
                        }
                    }
                    .cp-post-meta {
                        display: flex;
                        align-items: center;
                        flex-wrap: wrap;
                        transition: 0.25s;
                        color: var(--cs-color-meta);
                        font-family: var(--cs-font-post-meta-family), sans-serif;
                        font-size: var(--cs-font-post-meta-size);
                        font-weight: var(--cs-font-post-meta-weight);
                        font-style: var(--cs-font-post-meta-style);
                        letter-spacing: var(--cs-font-post-meta-letter-spacing);
                        text-transform: var(--cs-font-post-meta-text-transform);
                    }
                }
            }

            .cp-fund-goal {
                span {
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    text-decoration: none;
                    border: none;
                    border-radius: var(--cs-primary-border-radius);
                    line-height: 1rem;
                    transition: 0.25s;
                    box-shadow: none;
                    cursor: pointer;
                    padding: 0.75rem 1.5rem;
                    border-radius: var(--cs-primary-border-radius);
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
                    &:hover {
                        border: 1px solid var(--cs-color-style-hover-border);
                        background-color: var(--cs-color-style-hover);
                        color: var(--cs-color-style-hover-contrast);
                    }
                }
            }
        }
    }
}
</style>
