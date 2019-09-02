import React from "react"

import { Link } from "gatsby"

const Apps = () => {
  return (
    <div>
        <div
        className="apps-title"
        >
        Apps
        </div>
        <div
        className="apps-nav-bar"
        >
            -
            <Link
            style={{
                boxShadow: `none`,
                textDecoration: `none`,
                color: `inherit`,
            }}
            to={`/apps/refresher/app`}
            >
                Refresher 
            </Link>
            - -
            <Link
            style={{
                boxShadow: `none`,
                textDecoration: `none`,
                color: `inherit`,
            }}
            to={`/apps/periodictable/app`}
            >
                Periodic Table 
            </Link>
            -
        </div>
    </div>
  )
}

export default Apps
