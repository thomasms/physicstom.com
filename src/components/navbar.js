import React from "react"

import { Link } from "gatsby"

class NavBar extends React.Component {
  constructor(props) {
    super(props)

    this.toggleMenu = this.toggleMenu.bind(this)

    this.state = {
      activeMenu: false,
    }
  }

  toggleMenu() {
    this.setState((prevState, props) => {
      return { activeMenu: !prevState.activeMenu }
    })
  }

  render() {
    return (
      <div style={{ marginBottom: "40px" }}>
        <nav
          className="navbar is-fixed-top"
          role="navigation"
          aria-label="main navigation"
        >
          <div className="navbar-brand">
            <div
              role="button"
              aria-label="menu"
              aria-expanded="false"
              className={`navbar-burger burger ${
                this.state.activeMenu ? "is-active" : ""
              }`}
              datatarget="navbarMain"
              onClick={this.toggleMenu}
            >
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
            </div>
          </div>

          <div
            id="navbarMain"
            className={`navbar-menu ${
              this.state.activeMenu ? "is-active" : ""
            }`}
          >
            <div className="navbar-start">
              <Link
                style={{
                  boxShadow: `none`,
                  textDecoration: `none`,
                  color: `inherit`,
                }}
                to={`/`}
              >
                <div className="navbar-item">Home</div>
              </Link>

              <Link
                style={{
                  boxShadow: `none`,
                  textDecoration: `none`,
                  color: `inherit`,
                }}
                to={`/about`}
              >
                <div className="navbar-item">About</div>
              </Link>
            </div>

            <div className="navbar-end">
              <div className="navbar-item">
                <div className="buttons">
                  <Link
                    style={{
                      boxShadow: `none`,
                      textDecoration: `none`,
                      color: `inherit`,
                    }}
                    to={`/appsmain`}
                  >
                    <div className="button is-link is-rounded">Apps</div>
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </nav>
      </div>
    )
  }
}

export default NavBar
