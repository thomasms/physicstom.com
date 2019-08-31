import React from "react"
import { Link } from "gatsby"

import { rhythm, scale } from "../utils/typography"

import mainLogo from '../../content/assets/android-chrome-512x512.png'

class Layout extends React.Component {
  render() {
    const { location, title, children } = this.props
    const rootPath = `${__PATH_PREFIX__}/`
    let header

    if (location.pathname === rootPath) {
      header = (
        <h3
          style={{
            ...scale(1.5),
            fontFamily: `Montserrat, sans-serif`,
            color: `#1f3c88`,
            textAlign: `center`,
            marginLeft: `auto`,
            marginRight: `auto`,
            marginBottom: rhythm(1.5),
            marginTop: 0,
          }}
        >
          <Link
            style={{
              boxShadow: `none`,
              textDecoration: `none`,
              color: `inherit`,
            }}
            to={`/`}
          >
            <img  src={mainLogo} alt="logo" width="40px"/> {title}
          </Link>
        </h3>
      )
    } else {
      header = (
        <h3
          style={{
            fontFamily: `Montserrat, sans-serif`,
            marginTop: 0,
          }}
        >
          <Link
            style={{
              boxShadow: `none`,
              textDecoration: `none`,
              color: `inherit`,
            }}
            to={`/`}
          >
            {title}
          </Link>
        </h3>
      )
    }
    return (
      <div
        style={{
          fontFamily: `Montserrat, sans-serif`,
          marginLeft: `auto`,
          marginRight: `auto`,
          maxWidth: rhythm(44),
          padding: `${rhythm(1.5)} ${rhythm(3 / 4)}`,
        }}
      >
        <header>{header}</header>
        <main>{children}</main>
        <footer>
          © {new Date().getFullYear()}, Built with
          {` `}
          <a href="https://www.gatsbyjs.org">Gatsby</a>
        </footer>
      </div>
    )
  }
}

export default Layout
