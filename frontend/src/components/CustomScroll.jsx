import { useEffect } from 'react';
import { animateScroll as scroll } from 'react-scroll';

const CustomScroll = ({ children }) => {
  useEffect(() => {
    scroll.scrollToTop({
      duration: 500,
      smooth: true,
    });
  }, []);

  return <div>{children}</div>;
};

export default CustomScroll;