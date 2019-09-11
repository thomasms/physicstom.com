import React from "react"
import { graphql } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

class NotFoundPage extends React.Component {
  render() {
    const { data } = this.props
    const siteTitle = data.site.siteMetadata.title

    return (
      <Layout location={this.props.location} title={siteTitle}>
        <SEO title="About" />
        <h4>Some details about me....</h4>
        <p>
            I studied physics and mathematics a while ago. 
        </p>
        <p>
            I liked it so much I did a PhD in Particle Physics, during which I did a lot of programming.
        </p>
        <p>
            I then realised how powerful programming was and got a role as a Software Engineer at a company doing some stuff related to petrochemicals.
        </p>
        <p>
            I then learnt how to actually program, including all about testing and building production software.
        </p>
        <p>
            After some time I wanted a new challenge, and missed physics a bit.
        </p>
        <p>
            Now I am a nuclear scientist / software engineer, where I get to do: programming, physics, and research!
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
