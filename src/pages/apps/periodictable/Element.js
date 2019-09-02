import React from 'react';

function GridColourElement(props){

  const style = {
      gridColumn: props.gridPosition,
      gridColumnEnd: props.gridPosition,
      borderColor: props.colour
  };

  const atomic = props.element ? props.element.atomic : "";
  const symbol = props.element ? props.element.symbol : "";

  return(
    <div className="apps-periodictable-element"
          style={style}
          onMouseEnter={(element) => props.handleOnMouseEnter(props.element)}
          onMouseLeave={(element) => props.handleOnMouseLeave(props.element)}
          onClick={(element) => props.handleOnClick(props.element)}>
      <div className="apps-periodictable-element-atomic">
        {atomic}
      </div>
      <div className="apps-periodictable-element-symbol">
        {symbol}
      </div>
    </div>
  );
}

export default GridColourElement;
