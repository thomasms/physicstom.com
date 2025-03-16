import React from "react"
import { graphql } from "gatsby"

import Layout from "../components/layout"
import Seo from "../components/seo"

class NotFoundPage extends React.Component {
  render() {
    const { data } = this.props
    const siteTitle = data.site.siteMetadata.title

    return (
      <Layout location={this.props.location} title={siteTitle}>
        <Seo title="About" />
        <h4>Some details about me....</h4>
        <p>I studied physics and mathematics a while ago.</p>
        <p>
          Then I did a PhD in Particle Physics, which involved a lot of
          programming.
        </p>
        <p>
          I continue to do programming and develop software as much as I can
          before AI takes all the fun out of it.
        </p>
        <p>
          I am hoping there will still be some humans left in this business for
          the rest of my career, otherwise I will have to find something else to
          do..... like gardening.
        </p>
        <p>
          No, I don't like gardening. Perhaps, I will start a food truck
          business. I like food.
        </p>
      </Layout>
    )
  }
}

export default NotFoundPage

export const pageQuery = graphql`
  query {
    site {
      siteMetadata {
        title
        author
      }
    }
  }
`
