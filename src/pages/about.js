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
          I liked it so much I did a PhD in Particle Physics, during which I did
          a lot of programming.
        </p>
        <p>
          Realising how powerful programming was I got a role as a Software
          Engineer at a company doing some stuff related to petrochemicals.
        </p>
        <p>
          I then learnt how to <i>actually</i> program, including all about
          testing and building production software.
        </p>
        <p>
          After some time I wanted a new challenge, and missed physics a bit.
        </p>
        <p>
          Going back to physics I spent some time as a nuclear scientist /
          software engineer, where I got to do some work on some interesting
          projects in fusion research at UKAEA.
        </p>
        <p>
          I dabbled in HR as a data scientist building ML algorithms and doing
          application development (while trying to do some nuclear research on
          the side).
        </p>
        <p>
          Subsequently I joined the MYRRHA project and lead the software
          development of the control system at SCK CEN. After a while I got very
          frustrated with the bureaucracy and resigned.
        </p>
        <p>
          Now I am in a totally new domain of health care, again leading
          software development for a great start-up, spending considerable time
          writing Python and developing ETLs.
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
