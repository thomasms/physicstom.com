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
        <p>Then I did some more programming, but now for money.</p>
        <p>
          And now I write documents about software and programming for money.
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
