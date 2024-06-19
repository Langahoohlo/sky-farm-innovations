import Sidebar from '../../components/Sidebar';
import MainContent from '../../components/MainContent';

export default function DashBoard() {
  return (
    <div className="flex">
      <Sidebar />
      <MainContent />
    </div>
  );
}
